import pandas as pd
import glob
# Get a list of CSV files in your folder
files = glob.glob(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\20230*.csv')
# Create an empty list for DataFrames
dfs = []
# Loop through the files and read them into DataFrames
for f in files:
    df = pd.read_csv(f)
    dfs.append(df)
# Loop through the DataFrames and write them to Excel files
for i, df in enumerate(dfs):
    # Use the same name as the CSV file but change the extension
    excel_name = files[i].replace(".csv", ".xlsx")
    # Write the DataFrame to an Excel file
    df.to_excel(excel_name, index=None, header=True)