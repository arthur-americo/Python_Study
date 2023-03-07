#58 jogo da adivinhação
# o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.
import random
n = random.randint(0,10)
a = int(input('Digite um número entre 0 e 10: '))
for c in range(1,11):
    if a == n:
        print('Você acertou!')
        print ('Você precisou de {} tentativas para acertar.'.format(c))
        break
    else:
        a = int(input('Você errou! Tente novamente: '))
    if c == 10:
        print('Você perdeu!')
        print('O número era {}.'.format(n))
      