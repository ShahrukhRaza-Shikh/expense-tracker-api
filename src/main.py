from fastapi import FastAPI, HTTPException
from .models import ExpenseCreate
from .storage import load_expenses, save_expenses, get_next_id

app = FastAPI(
    title="Smart Expense Tracker API",
    version="1.0.0",
    description="REST API for managing personal expenses."
)


@app.get("/")
def home():
    return {"message": "Smart Expense Tracker API is running!"}


@app.post("/expenses")
def add_expense(expense: ExpenseCreate):
    expenses = load_expenses()

    new_expense = {
        "id": get_next_id(expenses),
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": str(expense.date)
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    return new_expense


@app.get("/expenses")
def get_expenses(category: str = None):
    expenses = load_expenses()

    if category:
        return [
            expense for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses


@app.get("/expenses/total")
def total_expenses(category: str = None):
    expenses = load_expenses()

    if category:
        total = sum(
            expense["amount"]
            for expense in expenses
            if expense["category"].lower() == category.lower()
        )
        return {"category": category, "total": total}

    total = sum(expense["amount"] for expense in expenses)
    return {"total": total}


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            return {"message": "Expense deleted successfully"}

    raise HTTPException(status_code=404, detail="Expense not found")