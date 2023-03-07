'''Make a program that reads a student's name and average, also saving the situation in a dictionary. 
At the end, show the contents of the structure on the screen.'''
student = {}
student['name'] = input('Name: ')
student['average'] = float(input(f'Average of {student["name"]}: '))
if student['average'] >= 7:
    student['situation'] = 'Approved'
elif 5 <= student['average'] < 7:
    student['situation'] = 'Recovery'
else:
    student['situation'] = 'Disapproved'
print('-=' * 30)
for k, v in student.items():
    print(f'{k} is equal to {v}')