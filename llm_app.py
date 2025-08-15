import streamlit as st
import json
import pandas as pd
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyCLgThQFZT9deF81aUrn1ja_E9Q2O1VQlk"


st.set_page_config(layout="wide")

st.title("Expense Tracker")

filename = "expenses.csv"


def add_expense(message):
    genai.configure(api_key=GOOGLE_API_KEY)

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
        model_name="gemini-2.5-flash", generation_config=generation_config
    )

    prompt_instructions = (
        "You extract a single expense from a user's message and return ONLY JSON. "
        "Return an object with fields: amount (number), category (string), note (string)."
    )

    response = model.generate_content([prompt_instructions, f"User message: {message}"])

    try:
        parsed = json.loads(response.text)
    except:
        st.error("Failed to parse expense")

    with open(filename, "a") as file:
        file.write(f"{parsed['amount']}, {parsed['category']}, {parsed['note']}\n")
        st.success("Expense added successfully")


def view_expense():
    df = pd.read_csv(filename)
    st.dataframe(df)


col1, col2 = st.columns(2, gap="large")

with col1:
    message = st.text_area("Message")

    if st.button("Submit"):
        add_expense(message)
        st.success("Expense added successfully")


with col2:
    view_expense()
