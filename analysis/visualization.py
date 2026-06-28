import matplotlib.pyplot as plt
import seaborn as sns

from cleaning import load_and_clean_data


df = load_and_clean_data("../data/online_shopping_behavior.csv")


plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=15)
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Customers")
plt.show()


plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Gender")
plt.title("Gender-wise Customers")
plt.show()


plt.figure(figsize=(10,5))
df["Category"].value_counts().plot(kind="bar")
plt.title("Product Categories")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(8,5))
df.groupby("Month")["Purchase Amount (USD)"].sum().plot(marker="o")
plt.title("Monthly Purchase Trend")
plt.ylabel("Revenue")
plt.show()


plt.figure(figsize=(6,5))
sns.boxplot(
    data=df,
    x="Discount Applied",
    y="Purchase Amount (USD)"
)
plt.title("Discount Impact")
plt.show()


plt.figure(figsize=(6,5))
sns.scatterplot(
    data=df,
    x="Review Rating",
    y="Purchase Amount (USD)"
)
plt.title("Ratings vs Purchase")
plt.show()


plt.figure(figsize=(6,6))
df["Payment Method"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Payment Methods")
plt.show()


plt.figure(figsize=(8,5))
sns.boxplot(
    data=df,
    x="Gender",
    y="Purchase Amount (USD)"
)
plt.title("Customer Spending")
plt.show()


plt.figure(figsize=(10,5))
df.groupby("Category")["Purchase Amount (USD)"].sum().sort_values().plot(kind="barh")
plt.title("Top Selling Categories")
plt.show()


plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="Age",
    y="Purchase Amount (USD)",
    hue="Gender"
)
plt.title("Customer Segmentation")
plt.show()