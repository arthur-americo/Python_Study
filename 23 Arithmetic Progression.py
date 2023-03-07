# #51 – Progressão Aritmética
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
n=int(input('Digite o primeiro termo: '))
n1=int(input('Digite a razão: '))
for c in range(1,11):
    print('{} -> '.format(n), end='')
    n+=n1
print('FIM')