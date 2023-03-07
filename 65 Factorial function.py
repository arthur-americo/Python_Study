'''Create a program that has a factorial function () that receives two parameters: 
the first to indicate the number to calculate and another called show, which will be a logical (optional) 
value indicating whether or not the factorial calculation process will be shown on the screen. .'''
def factorial(n, show=False):
    f = 1
    for i in range(n, 0, -1):
        if show:
            print(f'{i} x ' if i > 1 else f'{i} = ', end='')
        f *= i
    return f

n = int(input('Enter a number to calculate its factorial: '))
show = input('Show calculation process? (y/n): ').lower() == 'y'
print(factorial(n, show))