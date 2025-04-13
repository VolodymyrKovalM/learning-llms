import pandas as pd

file_path = "./sample_data/data.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

print(df.head(100))
