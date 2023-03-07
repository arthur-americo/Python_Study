n = float(input('Enter the employee's salary: ')) # Receives the employee's salary as a float
if n > 1250:
     increase = n * 0.10 # Calculates the increase of 10% for employees with salary higher than R$ 1250,00
else:
     increase = n * 0.15 # Calculates the increase of 15% for employees with salary lower than R$ 1250,00
print('The employee's salary is R${:.2f} and the raise was R${:.2f}'.format(n, increase))