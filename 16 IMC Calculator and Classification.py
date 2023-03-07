""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:	
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida """
n = float(input('Qual o seu peso? (Kg) '))
a = float(input('Qual a sua altura? (m) '))
imc = n / (a ** 2)
if imc < 18.5:
    print('Você está abaixo do peso e seu imc é de {}'.format (imc))
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal e seu imc é de {}'.format (imc))
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso e seu imc é de {}'.format (imc))
elif imc >= 30 and imc < 40:
    print('Você está com obesidade e seu imc é de {}'.format (imc))
else:
    print('Você está com obesidade mórbida e seu imc é de {}'.format (imc))

