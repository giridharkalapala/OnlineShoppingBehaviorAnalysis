import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Online Shopping Behavior Analysis",
    page_icon="🛒",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "online_shopping_behavior.csv")

df = pd.read_csv(DATA_PATH)

# -----------------------------
# Data Cleaning
# -----------------------------
df.drop_duplicates(inplace=True)

df.fillna(method="ffill", inplace=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Filters")

age = st.sidebar.slider(
    "Age",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (
        int(df["Age"].min()),
        int(df["Age"].max())
    )
)

gender = st.sidebar.multiselect(
    "Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

category = st.sidebar.multiselect(
    "Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

payment = st.sidebar.multiselect(
    "Payment Method",
    options=df["Payment Method"].unique(),
    default=df["Payment Method"].unique()
)

location = st.sidebar.multiselect(
    "Location",
    options=df["Location"].unique(),
    default=df["Location"].unique()
)

filtered = df[
    (df["Gender"].isin(gender)) &
    (df["Category"].isin(category)) &
    (df["Payment Method"].isin(payment)) &
    (df["Location"].isin(location)) &
    (df["Age"] >= age[0]) &
    (df["Age"] <= age[1])
]

# -----------------------------
# Title
# -----------------------------
st.title("🛒 Online Shopping Behavior Analysis Dashboard")

st.markdown("---")

# -----------------------------
# KPI Cards
# -----------------------------
c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Customers",
    filtered["Customer ID"].nunique()
)

c2.metric(
    "Orders",
    len(filtered)
)

c3.metric(
    "Revenue",
    f"${filtered['Purchase Amount (USD)'].sum():,.0f}"
)

c4.metric(
    "Average Order",
    f"${filtered['Purchase Amount (USD)'].mean():.2f}"
)

c5.metric(
    "Top Category",
    filtered["Category"].mode()[0]
)

st.markdown("---")

# -----------------------------
# Row 1
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        filtered,
        x="Age",
        nbins=20,
        title="Customer Age Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.pie(
        filtered,
        names="Gender",
        title="Gender-wise Purchases"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Row 2
# -----------------------------
col3, col4 = st.columns(2)

with col3:

    cat = filtered.groupby("Category")["Purchase Amount (USD)"].sum().reset_index()

    fig = px.bar(
        cat,
        x="Category",
        y="Purchase Amount (USD)",
        title="Category Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:

    pay = filtered["Payment Method"].value_counts().reset_index()

    pay.columns = ["Payment Method", "Orders"]

    fig = px.bar(
        pay,
        x="Payment Method",
        y="Orders",
        title="Payment Methods"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Row 3
# -----------------------------
col5, col6 = st.columns(2)

with col5:

    fig = px.box(
        filtered,
        x="Discount Applied",
        y="Purchase Amount (USD)",
        title="Discount Impact"
    )

    st.plotly_chart(fig, use_container_width=True)

with col6:

    fig = px.scatter(
        filtered,
        x="Review Rating",
        y="Purchase Amount (USD)",
        color="Gender",
        title="Ratings vs Purchase"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Monthly Trend
# -----------------------------
month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

filtered["Month"] = pd.Categorical(
    filtered["Month"],
    categories=month_order,
    ordered=True
)

trend = filtered.groupby("Month")["Purchase Amount (USD)"].sum().reset_index()

fig = px.line(
    trend,
    x="Month",
    y="Purchase Amount (USD)",
    markers=True,
    title="Monthly Purchase Trend"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Spending Pattern
# -----------------------------
fig = px.violin(
    filtered,
    x="Gender",
    y="Purchase Amount (USD)",
    box=True,
    title="Customer Spending Pattern"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Top Categories
# -----------------------------
top = filtered.groupby("Category")["Purchase Amount (USD)"].sum().reset_index()

top = top.sort_values(
    by="Purchase Amount (USD)",
    ascending=False
)

fig = px.bar(
    top,
    x="Purchase Amount (USD)",
    y="Category",
    orientation="h",
    title="Top Selling Categories"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Customer Segmentation
# -----------------------------
fig = px.scatter(
    filtered,
    x="Age",
    y="Purchase Amount (USD)",
    color="Category",
    size="Purchase Amount (USD)",
    hover_data=["Payment Method"],
    title="Customer Segmentation"
)

st.plotly_chart(fig, use_container_width=True)

#============================================================================================================================================================
# -----------------------------
# Raw Data
# -----------------------------
st.subheader("Dataset Preview")

st.dataframe(filtered)

st.success("Dashboard Loaded Successfully")