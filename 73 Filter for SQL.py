'''This code reads an Excel file into a pandas DataFrame and finds column names that appear more than once in the ‘COLUMN_NAME’ 
column. It then filters the DataFrame to only show rows with duplicate column names and selects the ‘TABLE_NAME’ and ‘COLUMN_NAME’ columns. 
The result is displayed using colorama for formatting and saved to a new Excel file.'''
import pandas as pd
from colorama import Fore, Back

# Ler o arquivo Excel em uma DataFrame do pandas
excel_Data = pd.read_excel(r'C:\Users\User\Desktop\Coisas\SQL\Tabelas 2.0\MvTablesAndColumns.xlsx')

# Encontrar os nomes das colunas que aparecem mais de uma vez na coluna 'COLUMN_NAME'
duplicate_columns = excel_Data[excel_Data.duplicated(['COLUMN_NAME'], keep=False)]['COLUMN_NAME'].unique()

# Filtrar as colunas duplicadas e selecionar as colunas desejadas
table_columns = excel_Data[excel_Data['COLUMN_NAME'].isin(duplicate_columns)][['TABLE_NAME', 'COLUMN_NAME']]

# Exibir o resultado
print(Back.WHITE + Fore.BLACK + f'{table_columns}' + Back.RESET + Fore.RESET)

print(Fore.WHITE + Back.RED + 'Aqui está meu patrão' + Back.RESET + Fore.RESET)
table_columns.to_excel('novo_excel.xlsx', sheet_name='Sheet1')


