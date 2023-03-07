#57 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
for c in range(1,2):
    if s in 'MF':
        print('Sexo {} registrado com sucesso!'.format(s))
        break
    else:
        s = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('FIM')