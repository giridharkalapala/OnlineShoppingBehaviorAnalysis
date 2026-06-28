import pandas as pd

from cleaning import load_and_clean_data


df = load_and_clean_data("../data/online_shopping_behavior.csv")


print("\n========== DATASET ==========")
print(df.head())


print("\n========== SHAPE ==========")
print(df.shape)


print("\n========== COLUMNS ==========")
print(df.columns)


print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


print("\n========== SUMMARY ==========")
print(df.describe())


print("\n========== CATEGORY COUNTS ==========")
print(df["Category"].value_counts())


print("\n========== GENDER ==========")
print(df["Gender"].value_counts())


print("\n========== PAYMENT ==========")
print(df["Payment Method"].value_counts())


print("\n========== CORRELATION ==========")
print(df.select_dtypes(include="number").corr())