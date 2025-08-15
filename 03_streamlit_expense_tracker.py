"""
Beginner-friendly Streamlit Expense Tracker

What this app shows:
- A simple UI to add and view expenses
- Reading and writing CSV with pandas
- Streamlit widgets and layout

Run locally:
  streamlit run 03_streamlit_expense_tracker.py

Helpful docs:
- Streamlit: https://docs.streamlit.io/
- pandas read_csv: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
- Streamlit Cheatsheet: https://docs.streamlit.io/develop/quick-reference/cheat-sheet
"""

import os
import pandas as pd
import streamlit as st


CSV_FILENAME = "expenses.csv"


def ensure_csv_exists(file_path: str) -> None:
    if os.path.exists(file_path):
        return
    pd.DataFrame(columns=["amount", "category", "note"]).to_csv(file_path, index=False)


def append_expense(amount, category, note, file_path):
    ensure_csv_exists(file_path)
    df = pd.DataFrame([{"amount": amount, "category": category, "note": note}])
    df.to_csv(file_path, mode="a", header=False, index=False)


def read_expenses(file_path: str) -> pd.DataFrame:
    ensure_csv_exists(file_path)
    return pd.read_csv(file_path)


st.set_page_config(page_title="Expense Tracker", layout="wide")
st.title("Expense Tracker")


col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Add Expense")
    amount = st.number_input("Amount", min_value=0.0, step=0.5, format="%.2f")
    category = st.text_input("Category")
    note = st.text_area("Note")

    if st.button("Submit", type="primary"):
        if amount <= 0:
            st.error("Amount must be greater than 0")
        elif not category.strip():
            st.error("Category is required")
        else:
            append_expense(amount, category.strip(), note.strip(), CSV_FILENAME)
            st.success("Expense added successfully")


with col2:
    st.subheader("View Expenses")
    df = read_expenses(CSV_FILENAME)
    st.dataframe(df, use_container_width=True)
