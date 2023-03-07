# 49 – Tabuada v.2.0
# mostre a tabuada de um numero que o usuario escolher. use um laço for
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print(f'{num} x {c} = {num*c}')