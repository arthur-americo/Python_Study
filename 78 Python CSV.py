import pandas as pd

# Load the CSV file
data = pd.read_csv(r'C:\Users\User\Desktop\Coisas\Trabalho\CSV\202301.csv', sep='|', header=None)

# Select the relevant columns
data = data[[0, 2, 4, 5, 6, 10, 17,18,19]]

# Convert columns 4 and 10 to datetime objects
data[4] = pd.to_datetime(data[4])
data[10] = pd.to_datetime(data[10])

# Format the dates as strings in the desired format
data[4] = data[4].dt.strftime('%Y-%m-%d')
data[10] = data[10].dt.strftime('%Y-%m-%d')

# Write the DataFrame to an Excel file
data.to_excel(r'C:\Users\User\Desktop\Coisas\Trabalho\CSV\202301.xlsx', index=False)
