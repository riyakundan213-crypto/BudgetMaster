import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="BudgetMaster India", layout="wide")

st.markdown("""
    <h1 style="text-align:center; color:#4D79FF;">💰 BudgetMaster India</h1>
    <h4 style="text-align:center; color:#888;">AI-Powered Budget & Expense Analyzer</h4>
    <br>
""", unsafe_allow_html=True)

st.sidebar.header("Upload or Enter Your Budget")

# Upload option
file = st.sidebar.file_uploader("Upload budget CSV (Category, Amount)", type=["csv"])

if file:
    df = pd.read_csv(file)
else:
    # Default sample
    df = pd.DataFrame({
        "Category": ["Rent", "Food", "Shopping", "Travel", "Entertainment", "Savings", "Bills & EMI"],
        "Amount": [15000, 6500, 3000, 2000, 1200, 5000, 4800]
    })

# Show table
st.subheader("📋 Budget Table")
st.dataframe(df, width=700)

# Pie Chart
st.subheader("📊 Spending Distribution")
fig1, ax1 = plt.subplots()
ax1.pie(df["Amount"], labels=df["Category"], autopct="%1.1f%%")
ax1.axis("equal")
st.pyplot(fig1)

# Bar Chart
st.subheader("📈 Expense Bar Chart")
fig2, ax2 = plt.subplots()
ax2.bar(df["Category"], df["Amount"])
plt.xticks(rotation=45)
st.pyplot(fig2)

# AI-based suggestions
total = df["Amount"].sum()
savings = df[df["Category"] == "Savings"]["Amount"].values[0]

st.subheader("🤖 AI Suggestions")
if savings < total * 0.20:
    st.warning("Increase your savings to at least **20%** of monthly income.")
else:
    st.success("Your savings ratio is healthy. Keep it up!")

# Summary
st.info(f"📌 Total Monthly Budget: **₹{total}**")
