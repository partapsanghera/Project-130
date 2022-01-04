import csv
import pandas as pd
import time

df=pd.read_csv("main.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv("final.csv")