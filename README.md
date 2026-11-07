# Flask & MongoDB Assignment

## Tasks implemented
- `GET /api`: reads a JSON list from `data.json` and returns it as JSON.
- `/`: displays a frontend form.
- `POST /submit`: validates fields and inserts a document into MongoDB Atlas.
- Successful insert redirects to `/success`, which displays **Data submitted successfully**.
- Validation or database errors are displayed on the form page without redirecting.

## Run in Ubuntu / WSL
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and set your real MongoDB Atlas URI.
python app.py
```
Open `http://127.0.0.1:5000/` in your browser and `http://127.0.0.1:5000/api` to test Task 1.

## MongoDB Atlas setup
1. Create a free Atlas cluster and a database user.
2. In Atlas Network Access, allow your current IP for this learning exercise. Avoid permanently allowing all IPs unless you understand the security implications.
3. Select Connect > Drivers and copy the Python connection string.
4. Put the connection string in `.env`, replacing the username, password, and cluster placeholder. URL-encode special characters in the password.
5. Never commit `.env` or share the connection string publicly.

## Before submission
- Capture real screenshots of the terminal, `/api` JSON response, form page, success page, and a saved document in Atlas.
- Add the screenshots and your own brief explanation to the documentation.
- Create a GitHub repository and add its URL to the documentation.
- Zip the complete project folder. Do not submit `.env`; submit `.env.example` instead.
