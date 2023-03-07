""" A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua 
categoria, de acordo com a idade:
- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 25 anos: SENIOR
- acima: MASTER"""
n = int(input('Em que ano você nasceu? '))
a = 2023 - n
if a <= 9:
    print('Você está na categoria MIRIM.')
elif a <= 14:
    print('Você está na categoria INFANTIL.')
elif a <= 19:
    print('Você está na categoria JUNIOR.')
elif a <= 25:
    print('Você está na categoria SENIOR.')
else:
    print('Você está na categoria MASTER.')
    