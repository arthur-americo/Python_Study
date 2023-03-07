n = int(input('Digite um número: '))
n1 = int(input('Digite outro número: '))
n2 = int(input('Digite mais um número: '))
# Verificando o menor valor
menor = n
if n1 < n and n1 < n2:
    menor = n1
if n2 < n and n2 < n1:
    menor = n2
# Verificando o maior valor
maior = n
if n1 > n and n1 > n2:
    maior = n1
if n2 > n and n2 > n1:
    maior = n2
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
