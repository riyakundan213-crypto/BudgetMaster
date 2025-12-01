import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="GovBudget AI", layout="wide")

st.markdown("""
    <h1 style="text-align:center; color:#0066CC;">🇮🇳 GovBudget AI</h1>
    <h3 style="text-align:center; color:#555;">India & Global Budget Analytics Dashboard</h3>
    <br>
""", unsafe_allow_html=True)

# Load India data
india_df = pd.read_csv("india_budget.csv")

st.header("📘 India Budget Overview")
st.dataframe(india_df, width=800)

# India pie chart
st.subheader("🧭 Sector Allocation (India)")
fig1, ax1 = plt.subplots()
ax1.pie(india_df["Amount"], labels=india_df["Sector"], autopct="%1.1f%%", startangle=140)
ax1.axis("equal")
st.pyplot(fig1)

# Bar chart
st.subheader("📊 India Budget Comparison")
fig2, ax2 = plt.subplots()
ax2.bar(india_df["Sector"], india_df["Amount"], color="#0066CC")
plt.xticks(rotation=45)
st.pyplot(fig2)

st.divider()

# Load global data
global_df = pd.read_csv("global_budget.csv")

st.header("🌎 Global Country Budget Comparison")
country = st.selectbox("Select a Country:", global_df["Country"].unique())

selected = global_df[global_df["Country"] == country]

st.dataframe(selected)

# Global bar chart
st.subheader(f"📊 Spending Distribution: {country}")
fig3, ax3 = plt.subplots()
ax3.bar(selected["Sector"], selected["Amount"], color="#FF9933")
plt.xticks(rotation=45)
st.pyplot(fig3)

# AI Suggestions
st.header("🤖 AI Insights")
highest = selected.iloc[selected["Amount"].idxmax()]

st.success(f"**{country}** invests the highest in **{highest['Sector']}**, with an allocation of **${highest['Amount']} Billion**.")

