import json
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

load_dotenv()

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"


def get_mongo_collection():
    """Create a MongoDB client using the Atlas URI stored in .env."""
    mongo_uri = os.getenv("MONGODB_URI")
    if not mongo_uri:
        raise RuntimeError(
            "MongoDB is not configured. Add your MongoDB Atlas URI to the .env file."
        )

    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    # Force a connection check so connection errors are caught during form submission.
    client.admin.command("ping")
    database_name = os.getenv("MONGODB_DATABASE", "flask_assignment")
    collection_name = os.getenv("MONGODB_COLLECTION", "submissions")
    return client[database_name][collection_name]


@app.route("/")
def home():
    return render_template("index.html", error=None, form_data={})


@app.route("/api")
def api():
    """Read a JSON list from data.json and return it as an API response."""
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("The JSON data must be a list.")
        return jsonify(data)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        app.logger.exception("Unable to load API data")
        return jsonify({"error": f"Unable to load API data: {error}"}), 500


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    form_data = {"name": name, "email": email, "message": message}

    if not name or not email or not message:
        return render_template(
            "index.html",
            error="Please complete all fields before submitting.",
            form_data=form_data,
        ), 400

    document = {"name": name, "email": email, "message": message}

    try:
        collection = get_mongo_collection()
        collection.insert_one(document)
        return redirect(url_for("success"))
    except (PyMongoError, RuntimeError, ValueError) as error:
        app.logger.exception("Unable to save form submission")
        # The same form page is shown, with the error message and entered values.
        return render_template(
            "index.html",
            error=f"Could not save your data. Check your MongoDB Atlas configuration and connection. Details: {error}",
            form_data=form_data,
        ), 500


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    # Local development only. Do not use Flask's debug server in production.
    app.run(host="127.0.0.1", port=5000, debug=True)
