import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Finance Analytics Dashboard", page_icon="💰", layout="wide")
st.title("💰 Finance Analytics Dashboard")
st.caption("Analyze income, expenses, savings, and monthly financial trends.")

@st.cache_data
def load_data():
    return pd.read_csv("finance_data.csv", parse_dates=["Date"])

df = load_data()
df["Month"] = df["Date"].dt.to_period("M").astype(str)

st.sidebar.header("Filters")
categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Category", categories)
start_date = st.sidebar.date_input("Start date", df["Date"].min().date())
end_date = st.sidebar.date_input("End date", df["Date"].max().date())

filtered = df[(df["Date"].dt.date >= start_date) & (df["Date"].dt.date <= end_date)]
if selected_category != "All":
    filtered = filtered[filtered["Category"] == selected_category]

income = filtered.loc[filtered["Type"] == "Income", "Amount"].sum()
expenses = filtered.loc[filtered["Type"] == "Expense", "Amount"].sum()
savings = income - expenses
c1, c2, c3 = st.columns(3)
c1.metric("Total Income", f"₹{income:,.0f}")
c2.metric("Total Expenses", f"₹{expenses:,.0f}")
c3.metric("Net Savings", f"₹{savings:,.0f}", delta=f"{(savings/income*100):.1f}% of income" if income else "N/A")

left, right = st.columns(2)
with left:
    st.subheader("Income vs Expenses by Month")
    monthly = filtered.pivot_table(index="Month", columns="Type", values="Amount", aggfunc="sum", fill_value=0).reset_index()
    if not monthly.empty:
        melt = monthly.melt(id_vars="Month", var_name="Type", value_name="Amount")
        st.plotly_chart(px.bar(melt, x="Month", y="Amount", color="Type", barmode="group", title="Monthly comparison"), use_container_width=True)
    else:
        st.info("No data for the selected filters.")
with right:
    st.subheader("Expenses by Category")
    exp = filtered[filtered["Type"] == "Expense"].groupby("Category", as_index=False)["Amount"].sum()
    if not exp.empty:
        st.plotly_chart(px.pie(exp, names="Category", values="Amount", hole=0.4), use_container_width=True)
    else:
        st.info("No expense data for the selected filters.")

st.subheader("Transaction Records")
st.dataframe(filtered.sort_values("Date", ascending=False), use_container_width=True, hide_index=True)
st.download_button("Download filtered data as CSV", filtered.to_csv(index=False).encode("utf-8"), "finance_data_filtered.csv", "text/csv")

st.markdown("---")
st.caption("Educational demo project. The included transactions are sample data, not real financial records.")
