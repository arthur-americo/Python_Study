import pandas as pd
#read the excel file
files = pd.read_excel(r"C:\Users\User\Desktop\Coisas\SQL\Tabelas 2.0\Extrações Finais\Final_HEF_Produção_e_Desempenho.xlsx")
# Create an empty list for DataFrames
dfs = []
# filter the duplicates
dfs.append(files.drop_duplicates(subset=['HospitalID', 'Data', 'Indicador', 'Tipo', 'Valor']))
# Write the final DataFrame to an excel file
pd.concat(dfs).to_excel(r'C:\Users\User\Desktop\Coisas\SQL\Tabelas 2.0\Extrações Finais\Filtrado_final.xlsx', index=False)