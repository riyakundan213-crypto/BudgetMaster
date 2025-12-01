import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- STYLING ----------------
st.set_page_config(page_title="GovBudget AI 2.0", layout="wide")

st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #0A0F24, #101C3D);
    color: white;
}

.reportview-container .main .block-container {
    padding-top: 2rem;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 18px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    transition: all 0.2s ease-in-out;
}

.card:hover {
    border: 1px solid #4D79FF;
    box-shadow: 0px 0px 20px rgba(77,121,255,0.4);
}

h1 {
    color: #4D79FF;
    text-shadow: 0px 0px 15px rgba(77,121,255,0.7);
}

.section-title {
    font-size: 26px;
    margin-top: 20px;
    color: #00E0FF;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>🌐 GovBudget AI 2.0</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#c9d1d9;'>Futuristic AI Dashboard for India & Global Budgets</h3><br>", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
india_df = pd.read_csv("india_budget.csv")
global_df = pd.read_csv("global_budget.csv")

# ---------------- INDIA BUDGET SECTION ----------------
st.markdown("<p class='section-title'>🇮🇳 India Budget Dashboard</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.dataframe(india_df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🧭 Sector Allocation (India)")
    fig1, ax1 = plt.subplots()
    ax1.pie(india_df["Amount"], labels=india_df["Sector"], autopct="%1.1f%%", startangle=140)
    ax1.axis("equal")
    st.pyplot(fig1)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 India Budget Bar Chart")
    fig2, ax2 = plt.subplots()
    ax2.bar(india_df["Sector"], india_df["Amount"], color="#4D79FF")
    plt.xticks(rotation=45)
    st.pyplot(fig2)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr style='border:1px solid #4D79FF;'>", unsafe_allow_html=True)

# ---------------- GLOBAL SECTION ----------------
st.markdown("<p class='section-title'>🌎 Global Country Budget Comparison</p>", unsafe_allow_html=True)

country = st.selectbox("Select a Country:", global_df["Country"].unique())

selected = global_df[global_df["Country"] == country]

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.dataframe(selected, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(f"📈 Spending Distribution: {country}")
    
    fig3, ax3 = plt.subplots()
    ax3.bar(selected["Sector"], selected["Amount"], color="#00E0FF")
    plt.xticks(rotation=45)
    st.pyplot(fig3)
    
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- AI INSIGHTS ----------------
st.markdown("<p class='section-title'>🤖 AI Insights</p>", unsafe_allow_html=True)

highest = selected.iloc[selected["Amount"].idxmax()]
st.success(f"**{country}** invests the most in **{highest['Sector']}** with **${highest['Amount']} Billion**.")

