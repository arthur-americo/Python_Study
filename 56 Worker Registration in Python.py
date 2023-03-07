'''Create a program that reads name, year of birth and work card and registers it (with age) in a dictionary. 
If by chance the CTPS is different from ZERO, the dictionary will also receive the year of hiring and the salary. 
Calculate and add, in addition to age, how many years the person will retire.'''
from datetime import datetime

current_year = datetime.now().year
person = {}

person['name'] = input('Name: ')
birth_year = int(input('Year of Birth: '))
person['age'] = current_year - birth_year
person['work_card'] = int(input('Work Card (0 if none): '))

if person['work_card'] != 0:
    person['year_of_hiring'] = int(input('Year of Hiring: '))
    person['salary'] = float(input('Salary: R$'))
    person['retirement'] = (person['year_of_hiring'] + 35) - birth_year

print(person)