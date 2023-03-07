""" Crie um programa que faça o computador jogar Jokenpô com você. """
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
Mirim = int(input('Qual é a sua jogada Mirim? '))
Loca = int(input('Qual é a sua jogada Loca? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)
print('-=' * 11)
if Loca == 0: # computador jogou PEDRA
    if Mirim == 0:
        print('EMPATE!')
    elif Mirim == 1:
        print('Mirim VENCE!')
    elif Mirim == 2:
        print('Loca VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif Loca == 1: # computador jogou PAPEL
    if Mirim == 0:
        print('Loca VENCE!')
    elif Mirim == 1:
        print('EMPATE!')
    elif Mirim == 2:
        print('Mirim VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif Loca == 2: # computador jogou TESOURA
    if Mirim == 0:
        print('Mirim VENCE!')
    elif Mirim == 1:
        print('Loca VENCE!')
    elif Mirim == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
        