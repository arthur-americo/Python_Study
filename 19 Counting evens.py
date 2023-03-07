# #47 – Contagem de pares
#Conte quantos números pares existem entre 1 e 50
thislist = [range(1, 50)]
count = 0
for c in range(1, 50):
    if c % 2 == 0:
        print(c)
        count += 1
    else:
        print('Não é par')
print(f'Existem {count} números pares entre 1 e 50')