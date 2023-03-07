'''#69 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
d = 0
n = 0
c = 0
continuar = input('Deseja continuar? (S/N) ').strip().upper()[0]
while continuar == 'S':
i = int(input('Digite a idade: '))
s = input('Digite o sexo (M/F): ').strip().upper()[0]
if s == 'F' and i < 20:
c += 1
if s == 'M':
d += 1
if i > 18:
n += 1
continuar = input('Deseja continuar? (S/N) ').strip().upper()[0]
print(f'Pessoas com mais de 18 anos: {n}')
print(f'Homens cadastrados: {d}')
print(f'Mulheres com menos de 20 anos: {c}')
print('Fim do programa')
    