# #46 – Contagem regressiva
#Mostre na tela uma contagem regressiva para o estouro de fogos de artificio indo de 10 a 0 com uma pausa de 1 segundo entre eles
from time import sleep
n = input('Quer começar? Sim ou Não? ')
if n == 'Sim':
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('FELIZ ANO NOVO!!!')
else:
    print('Fim do programa')


