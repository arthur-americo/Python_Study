'''Create a program that reads the name, gender and age of several people, storing each person's data in a dictionary 
and all dictionaries in a list. At the end, show: 
A) How many people were registered 
B) The average age 
C) A list of women 
D) A list of people above average age'''
people = []
women = []
above_average_age = []

while True:
    person = {}
    person['name'] = input('Name: ')
    person['gender'] = input('Gender [M/F]: ').upper()
    person['age'] = int(input('Age: '))
    people.append(person)

    if person['gender'] == 'F':
        women.append(person)

    continue_registering = input('Continue registering? [Y/N] ').upper()
    if continue_registering == 'N':
        break

total_people = len(people)
average_age = sum([person['age'] for person in people]) / total_people

for person in people:
    if person['age'] > average_age:
        above_average_age.append(person)

print(f'Total people registered: {total_people}')
print(f'Average age: {average_age:.2f}')
print(f'Women registered: {[woman["name"] for woman in women]}')
print(f'People above average age: {[person["name"] for person in above_average_age]}')