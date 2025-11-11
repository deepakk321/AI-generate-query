# AI-generate-query
This application is for generating the sql query based on schema and user prompt.

## Run the Streamlit app

Quick steps to run the Streamlit UI (Windows PowerShell):

1. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Provide your Google API key (choose one):

- For the current PowerShell session only:

```powershell
$env:GOOGLE_API_KEY = 'your_api_key_here'
```

- Or create a `.env` file in the project root with the line:

```
GOOGLE_API_KEY=your_api_key_here
```

The Streamlit app will automatically load `.env` if present.

4. Run the app:

```powershell
streamlit run streamlit_app.py
```

Open the browser to the address Streamlit prints (usually http://localhost:8501). The UI accepts a schema upload (or uses `schema.txt`) and a user query, then shows the generated SQL.

