import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Expense Approval System", layout="wide")

st.title("💰 Expense Approval System")

menu = st.sidebar.selectbox("Menu", [
    "Submit Expense",
    "View Expenses",
    "Update/Delete",
    "Manager Panel"
])

# =========================
# SUBMIT EXPENSE
# =========================
if menu == "Submit Expense":
    st.subheader("🧾 Submit Expense")

    name = st.text_input("Employee Name")
    amount = st.number_input("Amount", min_value=1.0)
    category = st.text_input("Category")
    desc = st.text_area("Description")
    date = st.text_input("Date (YYYY-MM-DD)")

    if st.button("Submit Expense"):
        data = {
            "employee_name": name,
            "amount": amount,
            "category": category,
            "description": desc,
            "date": date
        }

        res = requests.post(f"{BASE_URL}/expenses/", json=data)

        if res.status_code == 200:
            st.success("✅ Expense Submitted Successfully")
        else:
            st.error("❌ Failed to submit expense")


# =========================
# VIEW EXPENSES
# =========================
elif menu == "View Expenses":
    st.subheader("📄 All Expenses")

    res = requests.get(f"{BASE_URL}/expenses/")

    if res.status_code == 200:
        data = res.json()

        if data:
            for exp in data:
                st.card = st.container()
                with st.card:
                    st.write(f"🆔 ID: {exp['id']}")
                    st.write(f"👤 Name: {exp['employee_name']}")
                    st.write(f"💰 Amount: ₹{exp['amount']}")
                    st.write(f"📂 Category: {exp['category']}")
                    st.write(f"📝 Description: {exp['description']}")
                    st.write(f"📅 Date: {exp['date']}")
                    st.write(f"📌 Status: {exp['status']}")
                    st.markdown("---")
        else:
            st.info("No expenses found")

    else:
        st.error("Failed to fetch data")


# =========================
# UPDATE / DELETE
# =========================
elif menu == "Update/Delete":
    st.subheader("✏️ Update or Delete Expense")

    exp_id = st.number_input("Enter Expense ID", min_value=1, step=1)

    col1, col2 = st.columns(2)

    # UPDATE
    with col1:
        st.markdown("### Update Expense")

        name = st.text_input("New Name")
        amount = st.number_input("New Amount", min_value=1.0, key="upd_amt")
        category = st.text_input("New Category")
        desc = st.text_area("New Description")
        date = st.text_input("New Date")

        if st.button("Update"):
            data = {
                "employee_name": name,
                "amount": amount,
                "category": category,
                "description": desc,
                "date": date
            }

            res = requests.put(f"{BASE_URL}/expenses/{exp_id}", json=data)

            if res.status_code == 200:
                st.success("✅ Updated Successfully")
            else:
                st.error(res.json().get("detail", "Update failed"))

    # DELETE
    with col2:
        st.markdown("### Delete Expense")

        if st.button("Delete"):
            res = requests.delete(f"{BASE_URL}/expenses/{exp_id}")

            if res.status_code == 200:
                st.success("✅ Deleted Successfully")
            else:
                st.error(res.json().get("detail", "Delete failed"))


# =========================
# MANAGER PANEL
# =========================
elif menu == "Manager Panel":
    st.subheader("🧑‍💼 Manager Approval Panel")

    res = requests.get(f"{BASE_URL}/expenses/")

    if res.status_code == 200:
        data = res.json()

        if data:
            for exp in data:
                st.write(f"🆔 ID: {exp['id']} | 👤 {exp['employee_name']} | ₹{exp['amount']} | 📌 {exp['status']}")

                if exp["status"] == "Pending":
                    col1, col2 = st.columns(2)

                    # APPROVE
                    if col1.button(f"Approve {exp['id']}"):
                        res = requests.put(f"{BASE_URL}/expenses/{exp['id']}/approve")

                        if res.status_code == 200:
                            st.success(f"Expense {exp['id']} Approved")
                            st.rerun()
                        else:
                            st.error("Error approving")

                    # REJECT
                    if col2.button(f"Reject {exp['id']}"):
                        res = requests.put(f"{BASE_URL}/expenses/{exp['id']}/reject")

                        if res.status_code == 200:
                            st.success(f"Expense {exp['id']} Rejected")
                            st.rerun()
                        else:
                            st.error("Error rejecting")

                st.markdown("---")
        else:
            st.info("No expenses found")

    else:
        st.error("Failed to fetch expenses")