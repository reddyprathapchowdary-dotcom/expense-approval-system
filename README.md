# expense-approval-system
#  Expense Approval System

A backend application that simulates a real-world expense management workflow where employees submit expenses and managers approve or reject them.

## Overview
This project is designed to automate the expense approval process commonly used in organizations. It ensures proper tracking, validation, and control over expense submissions.

## Tech Stack
FastAPI – Backend framework
PostgreSQL – Database
SQLAlchemy – ORM (Object Relational Mapping)
Pydantic – Data validation
## Features
- Submit new expense requests
- View all expenses
- Update or delete pending expenses
- Approve or reject expenses (Manager role)
- Track status (Pending / Approved / Rejected)
- Proper validation and error handling
##  Workflow
1. Employee submits an expense  
2. Expense status is set to **Pending**  
3. Manager reviews the expense  
4. Manager approves or rejects  
5. Final status is updated in the system
   ##  System Flow (Step-by-Step)
###  Step 1: User Interaction
User (Employee) enters expense details in the frontend (Streamlit UI)
###  Step 2: Request Sent
Frontend sends an HTTP request to the FastAPI backend
###  Step 3: API Handling
FastAPI receives the request through an endpoint (POST /expenses/)
###  Step 4: Data Validation
Pydantic validates input data  
✔ Amount > 0  
✔ Required fields present  
###  Step 5: Business Logic
Backend checks rules  
✔ Status = Pending  
✔ Only valid operations allowed  
###  Step 6: Database Operation
SQLAlchemy ORM converts request into database query
###  Step 7: Data Storage
Data is stored in PostgreSQL database
###  Step 8: Response Generation
Database sends result back to backend
###  Step 9: API Response
FastAPI returns JSON response
###  Step 10: Display Output
Frontend displays updated data to user
##  Approval Process
###  Step 11: Manager Action
Manager reviews submitted expense
###  Step 12: Decision
Manager clicks Approve or Reject
###  Step 13: Status Update
Backend updates status in database (Approved / Rejected)
###  Step 14: Final Output
Updated status is shown in frontend 

##  API Endpoints

| Method | Endpoint | Description |
| POST | /expenses/ | Create expense |
| GET | /expenses/ | Get all expenses |
| GET | /expenses/{id} | Get single expense |
| PUT | /expenses/{id} | Update expense |
| DELETE | /expenses/{id} | Delete expense |
| PUT | /expenses/{id}/approve | Approve expense |
| PUT | /expenses/{id}/reject | Reject expense |

##  Business Logic
- Only Pending expenses can be updated or deleted  
- Approved/Rejected expenses cannot be modified  
- Amount must be greater than zero  
- Proper HTTP status codes are returned for errors  

##  Database Design
Table: expenses
Fields:
- id
- employee_name
- amount
- category
- description
- date
- status
##  Testing
- Tested using FastAPI Swagger UI  
- Data verified using PostgreSQL (pgAdmin)
    
##  Learning Outcomes
- Built REST APIs using FastAPI  
- Integrated PostgreSQL with SQLAlchemy  
- Implemented real-world business logic  
- Understood request-response lifecycle  

##  Future Enhancements
- Add authentication (JWT)
- Role-based access (Employee / Manager)
- Frontend using Streamlit
- Deploy the project online

##  Conclusion

## 🙌 Conclusion

The Expense Approval System demonstrates a complete backend application that handles real-world business workflows. It allows employees to submit expenses and enables managers to review, approve, or reject them efficiently.
Through this project, core backend concepts such as API development, database integration, and business rule enforcement were successfully implemented. The use of FastAPI, SQLAlchemy, and PostgreSQL ensures a scalable and structured system design.
Overall, this project reflects a strong understanding of how real-world enterprise applications manage data, enforce rules, and process user requests in a structured and reliable manner..
