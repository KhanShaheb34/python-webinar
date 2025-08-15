"""
Beginner-friendly LLM expense parser with Streamlit + Google Gemini

What this app shows:
- How to call a Generative AI model (Gemini) to parse free-text into JSON
- How to validate and save the result into a CSV
- Streamlit layout and feedback messages

IMPORTANT: You must set the Google API key as an environment variable before running:
  export GOOGLE_API_KEY="your_key_here"

Run locally:
  streamlit run 04_llm_expense_parser.py

Helpful docs:
- Gemini Python: https://ai.google.dev/gemini-api/docs
- JSON in Python: https://docs.python.org/3/library/json.html
- pandas read_csv: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
"""

import json
import os

import pandas as pd
import streamlit as st
import google.generativeai as genai


CSV_FILENAME = "expenses.csv"


def ensure_csv_exists(file_path: str) -> None:
    if os.path.exists(file_path):
        return
    pd.DataFrame(columns=["amount", "category", "note"]).to_csv(file_path, index=False)


def append_expense(amount, category, note, file_path):
    ensure_csv_exists(file_path)
    df = pd.DataFrame([{"amount": amount, "category": category, "note": note}])
    df.to_csv(file_path, mode="a", header=False, index=False)


def parse_message_with_gemini(message):
    """Use Gemini to parse a message and return a dict with amount/category/note, or None."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error(
            "Environment variable GOOGLE_API_KEY is not set. See the header of this file for setup."
        )
        return None

    genai.configure(api_key=api_key)

    generation_config = {
        "response_mime_type": "application/json",
        "response_schema": {
            "type": "object",
            "properties": {
                "amount": {"type": "number"},
                "category": {"type": "string"},
                "note": {"type": "string"},
            },
            "required": ["amount", "category", "note"],
        },
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        generation_config=generation_config,
    )

    system_prompt = (
        "Extract a single expense from the user's message and return ONLY JSON. "
        "Return an object with fields: amount (number), category (string), note (string)."
    )

    response = model.generate_content([system_prompt, f"User message: {message}"])

    try:
        parsed = json.loads(response.text)
        amount = float(parsed.get("amount", 0))
        category = str(parsed.get("category", "")).strip()
        note = str(parsed.get("note", "")).strip()
        if amount <= 0 or not category:
            return None
        return {"amount": amount, "category": category, "note": note}
    except Exception:
        return None


st.set_page_config(page_title="LLM Expense Parser", layout="wide")
st.title("LLM Expense Parser")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Describe your expense in natural language")
    example_hint = "Example: 'Had dinner for 18.50 at a local diner with friends'"
    message = st.text_area("Message", placeholder=example_hint)

    if st.button("Parse & Save", type="primary"):
        if not message.strip():
            st.error("Please enter a message.")
        else:
            result = parse_message_with_gemini(message.strip())
            if result is None:
                st.error(
                    "Could not parse a valid expense. Please try being more specific."
                )
            else:
                append_expense(
                    result["amount"], result["category"], result["note"], CSV_FILENAME
                )
                st.success("Expense parsed and saved successfully.")


with col2:
    st.subheader("Saved Expenses")
    ensure_csv_exists(CSV_FILENAME)
    df = pd.read_csv(CSV_FILENAME)
    st.dataframe(df, use_container_width=True)
