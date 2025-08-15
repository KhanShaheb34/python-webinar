# Python Mastery Through Micro Projects

This repo contains beginner-friendly Python projects built during the [webinar](https://interactivecares.com/events/micro-projects-python-mastery), in the following learning order:

1. `01_cli_expense_tracker.py` — Command-line interface (CLI) expense tracker
2. `02_fastapi_expense_tracker.py` — FastAPI expense tracker (in-memory)
3. `03_streamlit_expense_tracker.py` — Streamlit app writing/reading a CSV
4. `04_llm_expense_parser.py` — Streamlit + Google Gemini to parse natural language into expenses

All examples keep the code simple and well-commented for learners. Expenses are stored in a shared `expenses.csv` file in the project root.

## Quick Start

1. Create and activate a virtual environment (recommended)

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate  # Windows (PowerShell)
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Run each project

### CLI

- Add an expense:

  ```bash
  python 01_cli_expense_tracker.py add --amount 12.5 --category food --note "Lunch"
  ```

- View expenses:

  ```bash
  python 01_cli_expense_tracker.py view
  ```

### FastAPI (in-memory)

```bash
uvicorn 02_fastapi_expense_tracker:app --reload
# Open http://127.0.0.1:8000/docs for interactive API docs
```

### Streamlit

```bash
streamlit run 03_streamlit_expense_tracker.py
```

### LLM (Gemini) expense parser

- Get your API Key from: [Google AI Studio](https://aistudio.google.com/)
- Set your API key first:

  ```bash
  export GOOGLE_API_KEY="your_key_here"  # macOS/Linux
  # $env:GOOGLE_API_KEY="your_key_here" # Windows PowerShell
  ```

- Run the app:

  ```bash
  streamlit run 04_llm_expense_parser.py
  ```

## What You’ll Learn

- CLI: `argparse`, working with CSV files, basic functions and validation
- FastAPI: building APIs, Pydantic models, in-memory storage, interactive docs
- Streamlit: UI widgets, layouts, reading/writing CSV with pandas
- LLM: prompting Gemini to return structured JSON, validating and saving results

## File Overview

- `01_cli_expense_tracker.py`: Adds/views expenses via terminal
- `02_fastapi_expense_tracker.py`: API for adding/viewing expenses
- `03_streamlit_expense_tracker.py`: Web UI for adding/viewing expenses
- `04_llm_expense_parser.py`: Web UI where Gemini parses natural language into an expense

## Helpful Docs & Cheat Sheets

- Python

  - Official Docs: `https://docs.python.org/3/`
  - Tutorial: `https://docs.python.org/3/tutorial/`
  - Cheat Sheet: `https://www.pythoncheatsheet.org/`

- CLI

  - argparse: `https://docs.python.org/3/library/argparse.html`
  - csv module: `https://docs.python.org/3/library/csv.html`

- FastAPI

  - FastAPI: `https://fastapi.tiangolo.com/`
  - Pydantic: `https://docs.pydantic.dev/`
  - Uvicorn: `https://www.uvicorn.org/`

- Streamlit + Data

  - Streamlit: `https://docs.streamlit.io/`
  - pandas read_csv: `https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html`

- LLM (Gemini)
  - Gemini Python API: `https://ai.google.dev/gemini-api/docs`
  - JSON in Python: `https://docs.python.org/3/library/json.html`

If you need any resource that isn’t listed here, tell me which topic and I’ll add it.

## General Python Learning Resources

- Interactive Cares: `https://interactivecares.com/course/python-programming`
- Hukush-Pakush: `https://hukush-pakush.com/`
- Automate the Boring Stuff (free to read online): `https://automatetheboringstuff.com/`
- freeCodeCamp Python Course: `https://www.freecodecamp.org/learn/scientific-computing-with-python/`

## Notes

- The FastAPI app stores data in memory for simplicity, so data resets on server restart.
- The Streamlit and LLM apps persist to `expenses.csv` so you can see entries across runs.
- Keep your `GOOGLE_API_KEY` secret and never commit it to version control.
