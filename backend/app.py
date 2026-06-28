import pandas as pd
import os

from flask import Flask
from flask import render_template

from flask_login import LoginManager
from flask_login import login_required
from flask_login import current_user

from backend.database import db
from backend.models import User
from backend.auth import auth

from flask import send_file

import plotly.express as px
import plotly.io as pio


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

app.config["SECRET_KEY"] = "shopping_behavior_analysis"

db_path = os.path.join(BASE_DIR, "database", "users.db")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()

login_manager.login_view = "auth.login"

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):

    return User.query.get(int(user_id))


app.register_blueprint(auth, url_prefix="/auth")

# =======================
# Load Dataset
# =======================

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "online_shopping_behavior.csv"
)

df = pd.read_csv(DATA_PATH)

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/dashboard")
@login_required
def dashboard():

    total_customers = df["Customer ID"].nunique()

    total_orders = len(df)

    total_revenue = round(
        df["Purchase Amount (USD)"].sum(),
        2
    )

    average_order = round(
        df["Purchase Amount (USD)"].mean(),
        2
    )

    top_category = df["Category"].mode()[0]

    top_payment = df["Payment Method"].mode()[0]

    average_age = round(df["Age"].mean(), 1)

    highest_rating = round(df["Review Rating"].max(), 1)

    recent_orders = (
        df[
            [
                "Customer ID",
                "Category",
                "Purchase Amount (USD)",
                "Payment Method"
            ]
        ]
        .head(10)
        .to_dict(orient="records")
    )
    # -----------------------------
    # Plotly Charts
    # -----------------------------

    # Age Distribution
    fig_age = px.histogram(
        df,
        x="Age",
        nbins=20,
        title="Customer Age Distribution"
    )
    graph_age = pio.to_html(fig_age, full_html=False)

    # Gender Analysis
    fig_gender = px.pie(
        df,
        names="Gender",
        title="Gender-wise Purchases"
    )
    
    graph_gender = pio.to_html(fig_gender, full_html=False)

    # Category Revenue
    category_df = (
        df.groupby("Category")["Purchase Amount (USD)"]
        .sum()
        .reset_index()
    )

    fig_category = px.bar(
        category_df,
        x="Category",
        y="Purchase Amount (USD)",
        title="Category Revenue"
    )

    graph_category = pio.to_html(fig_category, full_html=False)
    
    # Monthly Purchase Trend
    month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    monthly_sales = (
        df.groupby("Month")["Purchase Amount (USD)"]
        .sum()
        .reindex(month_order)
        .reset_index()
    )

    fig_month = px.line(
        monthly_sales,
        x="Month",
        y="Purchase Amount (USD)",
        markers=True,
        title="Monthly Purchase Trend"
    )

    graph_month = pio.to_html(fig_month, full_html=False)
    
    # Discount Impact
    fig_discount = px.box(
        df,
        x="Discount Applied",
        y="Purchase Amount (USD)",
        color="Discount Applied",
        title="Discount Impact on Purchases"
    )

    graph_discount = pio.to_html(fig_discount, full_html=False)
    
    # Rating vs Purchase
    fig_rating = px.scatter(
        df,
        x="Review Rating",
        y="Purchase Amount (USD)",
        color="Category",
        title="Ratings vs Purchase Amount"
    )

    graph_rating = pio.to_html(fig_rating, full_html=False)

    # Customer Spending Pattern
    fig_spending = px.histogram(
        df,
        x="Purchase Amount (USD)",
        nbins=25,
        title="Customer Spending Pattern"
    )

    graph_spending = pio.to_html(fig_spending, full_html=False)

    # Top Selling Categories
    top_categories = (
        df["Category"]
        .value_counts()
        .reset_index()
    )

    top_categories.columns = ["Category", "Orders"]

    fig_top = px.bar(
        top_categories,
        x="Category",
        y="Orders",
        color="Category",
        title="Top Selling Categories"
    )

    graph_top = pio.to_html(fig_top, full_html=False)
    
    # Customer Segmentation
    fig_segment = px.scatter(
        df,
        x="Age",
        y="Purchase Amount (USD)",
        color="Gender",
        size="Purchase Amount (USD)",
        title="Customer Segmentation"
    )

    graph_segment = pio.to_html(fig_segment, full_html=False)

    return render_template(
        "dashboard.html",

        user=current_user,

        total_customers=total_customers,
        total_orders=total_orders,
        total_revenue=total_revenue,
        average_order=average_order,
        top_category=top_category,

        top_payment=top_payment,
        average_age=average_age,
        highest_rating=highest_rating,
        recent_orders=recent_orders,

        graph_age=graph_age,
        graph_gender=graph_gender,
        graph_category=graph_category,
        graph_payment=graph_payment,

        graph_month=graph_month,
        graph_discount=graph_discount,
        graph_rating=graph_rating,
        graph_spending=graph_spending,
        graph_top=graph_top,
        graph_segment=graph_segment,
    )


# Payment Method
payment_df = (
    df["Payment Method"]
    .value_counts()
    .reset_index()
)

payment_df.columns = ["Payment Method", "Orders"]

fig_payment = px.bar(
    payment_df,
    x="Payment Method",
    y="Orders",
    title="Payment Method Analysis"
)

graph_payment = pio.to_html(fig_payment, full_html=False)    

@app.route("/download")
@login_required
def download_dataset():

    return send_file(
        DATA_PATH,
        as_attachment=True,
        download_name="online_shopping_behavior.csv"
    )

with app.app_context():

    db.create_all()


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )

# =======================