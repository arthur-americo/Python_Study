'''#59Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
a1 = 'somar'
a2 = 'multiplicar'
a3 = 'maior'
a4 = 'novos números'
a5 = 'sair do programa'
for c in range(1,6):
    print('[{}] {}'.format (1, a1))
    print('[{}] {}'.format(2, a2))
    print('[{}] {}'.format(3, a3))
    print('[{}] {}'.format(4, a4))
    print('[{}] {}'.format(5, a5))
    break
c = int(input('Escolha uma das opções acima: '))
if c == 1:
    print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
elif c == 2:
    print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
elif c == 3:
    print('O maior número entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
elif c == 4:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
else:
    print ('FIM')
