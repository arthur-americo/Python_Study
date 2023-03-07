# #55 – Maior e menor da sequência  
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
n = input('Digite o nome da pessoa: ')
p = int(input('Digite o peso da pessoa: '))
n2 = input('Digite o nome da pessoa: ')
p2 = int(input('Digite o peso da pessoa: '))
n3 = input('Digite o nome da pessoa: ')
p3 = int(input('Digite o peso da pessoa: '))
n4 = input('Digite o nome da pessoa: ')
p4 = int(input('Digite o peso da pessoa: '))
n5 = input('Digite o nome da pessoa: ')
p5 = int(input('Digite o peso da pessoa: '))
for i in range(0, 5):
    if p > p2 and p > p3 and p > p4 and p > p5:
        print('O maior peso é de {} do {} e o menor peso é de {} do {}'.format(p, n, p2, n2))
    elif p2 > p and p2 > p3 and p2 > p4 and p2 > p5:
        print('O maior peso é de {} do {} e o menor peso é de {} do {}'.format(p2, n2, p, n))
    elif p3 > p and p3 > p2 and p3 > p4 and p3 > p5:
        print('O maior peso é de {} do {} e o menor peso é de {} do {}'.format(p3, n3, p, n))
    elif p4 > p and p4 > p2 and p4 > p3 and p4 > p5:
        print('O maior peso é de {} do {} e o menor peso é de {} do {}'.format(p4, n4, p, n))
    elif p5 > p and p5 > p2 and p5 > p3 and p5 > p4:
        print('O maior peso é de {} do {} e o menor peso é de {} do {}'.format(p5, n5, p, n))
    else:
        print('Os pesos são iguais')