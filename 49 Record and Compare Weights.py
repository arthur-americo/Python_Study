'''Make a program that reads name and weight of several people, keeping everything in a list. At the end, show: 
A) How many people were registered. 
B) A list of the heaviest people. 
C) A list of the lightest people.'''
# Create empty list
names = []

# User input
while True:
    print('Type the name and weight of the person')
    name = input('Name: ')
    weight = float(input('Weight: '))
    names.append([name, weight])
    print('Do you want to continue? [Y/N]')
    answer = input().upper()
    if answer == 'N':
        break

# Create a list with the heaviest people
names.sort(key=lambda x: x[1], reverse=True)
names_heaviest = [names[0]]

# List of the lightest people
names_lightest = [names[-1]]

# Print the lists
# All data registered
print(f'The number of people registered is {len(names)}')

# Heaviest person
print(f'The heaviest person is {names_heaviest}')

# Lightest person
print(f'The lightest person is {names_lightest}')

    