import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Expense Tracker")

filename = "expenses.csv"


def add_expense(amount, category, note):
    with open(filename, "a") as file:
        file.write(f"{amount}, {category}, {note}\n")


def view_expense():
    df = pd.read_csv(filename)
    st.dataframe(df)


col1, col2 = st.columns(2, gap="large")

with col1:
    amount = st.number_input("Amount")
    category = st.text_input("Category")
    notes = st.text_area("Notes")

    if st.button("Submit"):
        add_expense(amount, category, notes)
        st.success("Expense added successfully")


with col2:
    view_expense()
