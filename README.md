# NASA Exoplanet AI Local Demo

This project is a fully local setup for the NASA Space Apps Challenge "A World Away: Hunting for Exoplanets with AI".

## Structure
- `frontend/index.html` — Frontend page
- `frontend/style.css` — CSS
- `frontend/script.js` — JS
- `backend.py` — Python Flask backend running locally
- `README.md` — Instructions

## Instructions

### 1. Install Python dependencies
pip install flask pandas numpy

### 2. Start the backend
python backend.py
- This will run the backend at http://127.0.0.1:5000

### 3. Open the frontend
- Open `frontend/index.html` in a browser
- Upload a CSV file with a `flux` column
- The frontend will send the file to the local backend and display predictions

### 4. Notes
- Currently uses a **dummy AI** (random 0/1) for demonstration
- I'll replace `dummy_predict` with a trained AI model later when it finish the training
