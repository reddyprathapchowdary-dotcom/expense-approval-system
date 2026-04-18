from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

# 🔥 CREATE TABLES IN POSTGRESQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/create-table")
def create_table():
    from database import engine
    from models import Base
    Base.metadata.create_all(bind=engine)
    return {"message": "Table created"}


# 🔹 DATABASE SESSION
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 ROOT
@app.get("/")
def read_root():
    return {"message": "Expense Approval System API is running 🚀"}


# 🔹 CREATE EXPENSE
@app.post("/expenses/")
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = models.Expense(**expense.dict())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


# 🔹 GET ALL EXPENSES
@app.get("/expenses/")
def get_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()


# 🔹 GET SINGLE EXPENSE
@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    exp = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")

    return exp


# 🔹 UPDATE EXPENSE (ONLY IF PENDING)
@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, updated: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    exp = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")

    if exp.status != "Pending":
        raise HTTPException(status_code=400, detail="Cannot update non-pending expense")

    exp.employee_name = updated.employee_name
    exp.amount = updated.amount
    exp.category = updated.category
    exp.description = updated.description
    exp.date = updated.date

    db.commit()
    return {"message": "Expense updated"}


# 🔹 DELETE EXPENSE (ONLY IF PENDING)
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    exp = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")

    if exp.status != "Pending":
        raise HTTPException(status_code=400, detail="Cannot delete non-pending expense")

    db.delete(exp)
    db.commit()
    return {"message": "Expense deleted"}


# 🔹 APPROVE
@app.put("/expenses/{expense_id}/approve")
def approve_expense(expense_id: int, db: Session = Depends(get_db)):
    exp = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")

    exp.status = "Approved"
    db.commit()
    return {"message": "Approved"}


# 🔹 REJECT
@app.put("/expenses/{expense_id}/reject")
def reject_expense(expense_id: int, db: Session = Depends(get_db)):
    exp = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if not exp:
        raise HTTPException(status_code=404, detail="Expense not found")

    exp.status = "Rejected"
    db.commit()
    return {"message": "Rejected"}