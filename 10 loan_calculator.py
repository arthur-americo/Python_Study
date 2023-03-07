"""escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. o programa vai perguntar o valor da casa,
 o salario do comprador e em quantos anos ele vai pagar. 
calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado."""
n = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o seu salário? R$'))
a = int(input('Em quantos anos você vai pagar? '))
p = n / (a * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(n, a, p))