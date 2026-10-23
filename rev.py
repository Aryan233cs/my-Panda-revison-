from fileinput import filename
from os import read

import pandas as pd
from pandas import read_csv

expenses = [
    {"date": "2026-10-01", "category": "food",      "amount": 250, "note": "lunch"},
    {"date": "2026-10-02", "category": "transport", "amount": 80,  "note": "bus"},
    {"date": "2026-10-03", "category": "food",      "amount": 400, "note": "dinner"},
    {"date": "2026-11-01", "category": "books",     "amount": 600, "note": "python book"},
]

df = pd.DataFrame(expenses)          # list of dicts -> table
#print(df)
#print(df.shape)                      # (4, 4)
#print(df.dtypes)                     # type of each column
#df.info()                            # summary: columns, types, missing values
#print(df["amount"])
#print(df[df["category"]=="food"])
#print(df[(df["category"] == "food") & (df["amount"] > 300)])

df["date"]=pd.to_datetime(df["date"])
print(df["date"].dtypes)
df.to_csv("expense.csv",index=False)
df2=read_csv("expense.csv",parse_dates=["date"])
#print(df2.head())
print(df2.dtypes)
#print(df["date"].dt.month)
#print(df[(df["date"].dt.month ==10) & (df["amount"]> 249)])
su=df[df["date"].dt.month ==10]
print(su["amount"].sum())
print(df[df["amount"] > 300]["amount"].sum())