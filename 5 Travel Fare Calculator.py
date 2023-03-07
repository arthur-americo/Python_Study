n = float(input('Digite a distância da viagem em Km: '))
if n <= 200:
    preço = n * 0.50
else:
    preço = n * 0.45
print('O preço da passagem é R${:.2f}'.format(preço))

