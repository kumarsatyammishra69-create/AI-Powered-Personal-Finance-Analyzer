import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.prediction import predict
from src.utils import get_summary

st.set_page_config(page_title="Finance Analyzer", page_icon="💰", layout="wide")
st.title("💰 AI Personal Finance Analyzer")

# ── Upload CSV ──
st.subheader("📁 Upload Your Finance Data")
uploaded = st.file_uploader("Upload CSV file", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)
    st.success("File uploaded successfully!")
    st.dataframe(df.head(10))

    # ── Summary ──
    st.subheader("📊 Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Records",   len(df))
    col2.metric("Total Spent",     f"₹{df['Amount'].sum():,.2f}")
    col3.metric("Avg Transaction", f"₹{df['Amount'].mean():,.2f}")
    col4.metric("Top Category",    df['Category'].value_counts().idxmax())

    # ── Charts ──
    st.subheader("📈 Spending by Category")
    fig1 = px.bar(df, x='Category', y='Amount',
                  color='Category', title='Spending by Category')
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("🥧 Expense Distribution")
    fig2 = px.pie(df, names='Category', values='Amount',
                  title='Expense Distribution')
    st.plotly_chart(fig2, use_container_width=True)

# ── Predict ──
st.subheader("🔮 Predict Expense Category")
col1, col2 = st.columns(2)
with col1:
    amount = st.number_input("Amount (₹)", min_value=0.0, step=100.0)
    month  = st.slider("Month", 1, 12, 1)
with col2:
    dow    = st.slider("Day of Week (0=Mon, 6=Sun)", 0, 6, 0)
    is_wknd = 1 if dow >= 5 else 0
    st.info(f"Weekend: {'Yes' if is_wknd else 'No'}")

if st.button("🔮 Predict Category"):
    try:
        result = predict(amount, month, dow, is_wknd)
        st.success(f"✅ Predicted Category: **{result}**")
    except Exception as e:
        st.error(f"Error: {e} — Run main.py first to train the model!")


