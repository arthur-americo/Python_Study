'''Create a program that has the ReadINT () function, which will work similarly to Python's Input () function, 
but validating only one numerical value. Ex: n = ReadINT (‘Enter one N:‘)'''
def ReadINT(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('Error: please enter a valid integer.')

n = ReadINT('Enter an integer: ')
print(f'You entered: {n}')