'''Create a program where the user can type several numerical values and register them in a list. 
If the number already exists there, it will not be added. At the end, all unique values entered will be displayed, 
in ascending order.'''
# Create a list
List = []
#User input
while True:
    n = int(input('Type a number: '))
    if n not in List:
        List.append(n)
    else:
        print('This number already exists in the list.')
    r = str(input('Do you want to continue? [Y/N] '))
    if r in 'Nn':
        break
    #Sort the list
    List.sort()
    #Print the list
    print(f'You typed the numbers {List}')
    
    

