'''Create a program that will read several numbers and put them in a list. After that show:
A) How many numbers were entered.
B) The list of values, sorted in descending order. 
C) If the value 5 was typed and is or is not in the list.'''
# Create a list
lst = []

# User input
while True:
    n = int(input('Type a number: '))
    lst.append(n)
    r = input('Do you want to continue? [Y/N] ')
    if r.lower() == 'n':
        # ordered list
        lst.sort(reverse=True)
        print(f'You typed the numbers {lst}')
        # count the numbers entered
        print(f'You typed {len(lst)} numbers')
        # check if the number 5 is in the list
        print(f'The number 5 is {"not " if 5 not in lst else ""}in the list')
        break
