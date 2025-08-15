"""
Beginner-friendly FastAPI Expense Tracker (in-memory)

What this script shows:
- How to create a FastAPI app with endpoints
- Pydantic models for request/response validation
- Simple in-memory storage (resets on restart)

Run locally:
  uvicorn 02_fastapi_expense_tracker:app --reload

Open docs (interactive):
  http://127.0.0.1:8000/docs

Helpful docs:
- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- Uvicorn: https://www.uvicorn.org/
"""

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="Expense Tracker API", description="Simple API to add and view expenses"
)


class Expense(BaseModel):
    amount: float = Field(..., gt=0, description="Amount spent, must be > 0")
    category: str = Field(
        ..., min_length=1, description="Category such as food, travel"
    )
    note: str = Field("", description="Optional note")


# In-memory "database" just for demo purposes
expenses: List[Expense] = []


@app.get("/", summary="Health/Welcome")
def hello() -> dict:
    """Welcome route for quick testing."""
    return {"message": "Welcome to Expense Tracker API"}


@app.post("/add", response_model=Expense, summary="Add an expense")
def add_expense(expense: Expense) -> Expense:
    """Add an expense to the in-memory list and return it back."""
    expenses.append(expense)
    return expense


@app.get("/view", response_model=List[Expense], summary="View all expenses")
def view_expenses() -> List[Expense]:
    """Return all expenses currently in memory."""
    return expenses
