# #53 – Detector de Palíndromo
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos: MIRIM
n = str(input('Digite uma frase ou palavra: ')).strip().upper()
if n == n[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')