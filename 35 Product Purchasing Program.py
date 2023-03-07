'''70 Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai 
# continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
c = 0
p = 0
n = 0
continuar = input('Deseja continuar? (S/N) ').strip().upper()[0]
while continuar == 'S':
    n = input('Digite o nome do produto: ')
    p = float(input('Digite o preço do produto: '))
    continuar = input('Deseja continuar? (S/N) ').strip().upper()[0]
    if continuar == 'N':
    print('Você gastou R${p:.2f} com {n}')
    break