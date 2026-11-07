# Assignment 3: Flask & MongoDB

**Student name:** Naveen  
**Environment:** Ubuntu on WSL  
**GitHub repository:** Add your repository URL here after creating it.

## Objective
Build a Flask application with a JSON API route and a frontend form that stores submitted data in MongoDB Atlas, with success and error handling.

## Task 1 — JSON API Route
The `/api` route opens `data.json`, loads the JSON list with Python's `json` module, and returns the list through Flask's `jsonify()` function. If the file is missing or invalid, the route returns a JSON error and HTTP 500 status.

**Test command:**
```bash
curl http://127.0.0.1:5000/api
```

**Screenshot to insert:** Terminal showing the curl command and JSON output, or browser showing `http://127.0.0.1:5000/api`.

## Task 2 — Frontend Form with MongoDB Atlas
The home page displays a form for name, email, and message. On submission, Flask validates the fields and inserts the document into the configured MongoDB Atlas collection. If the insert succeeds, the browser is redirected to `/success`, which displays “Data submitted successfully”. If validation or database access fails, the form page is rendered again with an error message.

**Screenshots to insert:**
1. Form page at `http://127.0.0.1:5000/`.
2. Success page after a successful MongoDB Atlas insert.
3. The inserted document in MongoDB Atlas.
4. Error displayed on the same form page (you can test with an intentionally invalid or missing `.env` URI, then restore the correct URI).

## Commands used
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

## Result
Task 1 and Task 2 are implemented. Complete the live tests, insert your screenshots, and add your GitHub repository URL before submission.
