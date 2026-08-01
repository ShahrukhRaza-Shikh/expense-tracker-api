# Smart Expense Tracker API

A REST API built using FastAPI to manage personal expenses.

## Features

- Add Expense
- View All Expenses
- Filter by Category
- Calculate Total Expenses
- Delete Expense

## Installation

```bash
pip install -r requirements.txt
```

## Run Server

```bash
uvicorn src.main:app --reload
```

## Run Tests

```bash
pytest
```

## API Endpoints

| Method | Endpoint |
|---------|----------|
| GET | / |
| POST | /expenses |
| GET | /expenses |
| GET | /expenses/total |
| DELETE | /expenses/{expense_id} |

## Swagger Documentation

Open:

http://127.0.0.1:8000/docs
