import pandas as pd
import numpy as np
df = pd.read_csv("brudne_sprzedaz.csv",decimal=",")

pd.set_option('display.max_columns', None)
print(df.head(10))

df = df.dropna(how="all")
df = df.replace(["ERROR", "UNKNOWN"], np.nan)

df["Transaction ID"] = df["Transaction ID"].str.replace("TXN_","")
df["Transaction ID"] = pd.to_numeric(df["Transaction ID"], errors = "coerce")
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce").dt.date

df["Total Spent"] = df["Total Spent"].fillna(df["Quantity"] * df["Price Per Unit"])
df["Quantity"] = df["Quantity"].fillna(df["Total Spent"]/df["Price Per Unit"])
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Total Spent"] / df["Quantity"])


df = df.dropna(subset=["Total Spent"])
df = df.dropna(subset=["Item", "Quantity"], how="all")

print(df.isnull().sum())
print(df.info())



df.to_excel("czyste_sprzedaz.xlsx", index = False)
