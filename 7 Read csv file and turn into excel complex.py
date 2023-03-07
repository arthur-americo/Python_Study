'''This code reads a set of CSV files from a folder, selects specific columns and renames them. It then writes each file to an Excel file 
and concatenates all the data into a final DataFrame. It filters the final DataFrame to include rows with specific IDs, groups the data by 
date and type, counts the number of occurrences, pivots the results and writes them to separate Excel files based on the ID.'''
import pandas as pd
import glob

# Get a list of CSV files in your folder
files = glob.glob(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\20230*.csv')

# Create an empty list for DataFrames
dfs = []

# Loop through the files and read them into DataFrames
for f in files:
    # Read only rows 1, 5 and 22 (assuming zero-based indexing)
    df = pd.read_csv(f).iloc[:, [0, 4, 21]]
    # Rename the columns to ID, date and type 
    df.columns = ['ID', 'date', 'type']
    dfs.append(df)

# Loop through the DataFrames and write them to Excel files
for i, df in enumerate(dfs):
    df.to_excel(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\new{}.xlsx'.format(i), index=False, header=True)

# Concatenate all the DataFrames into one DataFrame
final_df = pd.concat(dfs)
# F I N A L
# Write the final DataFrame to an excel file with the same header
final_df.to_excel(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\final.xlsx', index=False)

# Filter the final DataFrame to only include rows where ID == 16
filtered_df = final_df[final_df['ID'] == 16]
# Write the filtered DataFrame to an excel file with the same header
filtered_df.to_excel(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\filtered.xlsx', index=False)
# Group by date and type and count the number of occurrences
result = filtered_df.groupby(['date', 'type']).size().reset_index(name='count')
# Pivot the result to get a DataFrame with dates as rows and types as columns
result = result.pivot(index='date', columns='type', values='count').fillna(0).astype(int)
# Write the result to an Excel file
result.to_excel(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\result_16.xlsx', index=True)   

# Filter the final DataFrame to only include rows where ID == 21
filtered_df = final_df[final_df['ID'] == 21]
# Write the filtered DataFrame to an excel file with the same header
filtered_df.to_excel(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\filtered.xlsx', index=False)
# Group by date and type and count the number of occurrences
result = filtered_df.groupby(['date', 'type']).size().reset_index(name='count')
# Pivot the result to get a DataFrame with dates as rows and types as columns
result = result.pivot(index='date', columns='type', values='count').fillna(0).astype(int)
# Write the result to an Excel file
result.to_excel(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\result_21.xlsx', index=True)  

# Filter the final DataFrame to only include rows where ID == 26
filtered_df = final_df[final_df['ID'] == 26]
# Write the filtered DataFrame to an excel file with the same header
filtered_df.to_excel(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\filtered.xlsx', index=False)
# Group by date and type and count the number of occurrences
result = filtered_df.groupby(['date', 'type']).size().reset_index(name='count')
# Pivot the result to get a DataFrame with dates as rows and types as columns
result = result.pivot(index='date', columns='type', values='count').fillna(0).astype(int)
# Write the result to an Excel file
result.to_excel(r'C:\Users\User\Desktop\saidahospitalarraw-20230301T120142Z-001\result_26.xlsx', index=True)  