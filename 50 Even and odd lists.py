'''Create a program where the user can enter seven numeric values and register them in a single 
list that keeps even and odd values separate. At the end, show the even and odd values in ascending order.'''
numbers = [[], []]
for i in range(7):
    n = int(input(f'Enter the {i+1}º number: '))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

numbers[0].sort()
numbers[1].sort()

print(f'The even numbers entered were: {numbers[0]}')
print(f'The odd numbers entered were: {numbers[1]}')