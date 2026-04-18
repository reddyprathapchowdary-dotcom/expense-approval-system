from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
    employee_name: str
    amount: float = Field(gt=0)
    category: str
    description: str
    date: str

class ExpenseUpdate(BaseModel):
    employee_name: str
    amount: float = Field(gt=0)
    category: str
    description: str
    date: str