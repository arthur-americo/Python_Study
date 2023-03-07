""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """
n = int(input('Em que ano você nasceu? '))
a = 2023 - n
if a < 18:
    print('Você ainda não precisa se alistar. Faltam {} anos.'.format(18 - a))
elif a == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você já deveria ter se alistado há {} anos.'.format(a - 18))
    2001