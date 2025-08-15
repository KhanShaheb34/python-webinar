from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Expense(BaseModel):
    amount: float
    category: str
    note: str


expenses = []


@app.get("/")
def hello():
    return {"message": "Welcome"}


@app.post("/add")
def add_expense(expense: Expense):
    expenses.append(expense)
    return expense


@app.get("/view")
def view_expenses():
    return expenses
