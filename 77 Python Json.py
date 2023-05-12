import json
import pandas as pd

# Load the JSON file
with open(r"C:\Users\User\Desktop\Coisas\Trabalho\CSV\regnet_hcn_2022.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract the relevant information for each paciente
pacientes = []
for paciente in data['models']:
    paciente_info = {'id': paciente['id']}
    if 'paciente' in paciente and 'pessoaFisica' in paciente['paciente']:
        if 'nome' in paciente['paciente']['pessoaFisica']:
            paciente_info['nome'] = paciente['paciente']['pessoaFisica']['nome']
        if 'cpf' in paciente['paciente']['pessoaFisica']:
            paciente_info['cpf'] = paciente['paciente']['pessoaFisica']['cpf']
    if 'dataSolicitacao' in paciente:
        paciente_info['dataSolicitacao'] = paciente['dataSolicitacao']
    if 'dataProcedimento' in paciente:
        paciente_info['dataProcedimento'] = paciente['dataProcedimento']
    pacientes.append(paciente_info)


# Create a DataFrame from the extracted information
df = pd.DataFrame(pacientes)

# Write the DataFrame to an Excel file
df.to_excel(r"C:\Users\User\Desktop\Coisas\Trabalho\CSV\pacientes.xlsx", index=False)
