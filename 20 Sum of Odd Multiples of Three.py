# Calcular a soma de todos os números múltiplos de três entre 1 e 500
count = 0
for c in range(1, 500):
    if c % 3 == 0:
        print(c)
        count += 1
print(f'Existem {count} números ímpares múltiplos de três entre 1 e 500')
# add print(f'Existem {n} números ímpares não múltiplos de três entre 1 e 500')
n = 500 - count
print (f'Existem {n} números ímpares não múltiplos de três entre 1 e 500')
