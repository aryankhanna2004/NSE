import pandas as pd
import glob

files = glob.glob('Nse_xlsx/*.xlsx')  # Modify the path as per your file location

dataframes = []

for file in files:
    df = pd.read_excel(file)
    dataframes.append(df)

merged = pd.concat(dataframes)

merged.to_excel("merged.xlsx")

