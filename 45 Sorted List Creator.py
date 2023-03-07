'''Create a program where the user can enter five numerical values and register them in a list, already in the correct 
insertion position (without using sort()). At the end, show the sorted list on the screen.
'''
# Create a list
list = []
# User input
while True:
    n = int(input('Type a number: '))
    if len(list) == 0 or n > list[-1]:
        list.append(n)
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                break
            pos += 1
    r = str(input('Do you want to continue? [Y/N] '))
    if r in 'Nn':
        break
    # Print the list
    print(f'You typed the numbers {list}')

    

