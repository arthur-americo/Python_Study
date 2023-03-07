'''Create a program that reads the name and two grades of several students and stores them all in a composite list. 
At the end, show a bulletin containing the average of each one and allow the user to show the grades of each student
individually.'''
# Creating a list to store the data
students = []
# Creating a while loop to repeat the data entry
while True:
    # Requesting the name of the student
    name = input('Name: ')
    # Requesting the first grade of the student
    grade1 = float(input('Grade 1: '))
    # Requesting the second grade of the student
    grade2 = float(input('Grade 2: '))
    # Calculating the average between the two grades
    avg = (grade1 + grade2) / 2
    # Adding the name, grades and average to the list
    students.append([name, [grade1, grade2], avg])
    # Asking if the user wants to add another student
    cont = input('Do you want to continue? [Y/N] ')
    # If the user doesn't want to add another student, stop the while loop
    if cont in 'Nn':
        break
# Printing a line to separate the data from the header
print('-=' * 30)
# Printing the header
print(f'{"No.":<4}{"NAME":<10}{"AVERAGE":>8}')
# Printing a line to separate the header from the data
print('-' * 26)
# Iterating over the students list, printing the student number, name and average
for i, student in enumerate(students):
    print(f'{i:<4}{student[0]:<10}{student[2]:>8.1f}')
# Creating another while loop to show the grades of a student
while True:
    # Printing a line to separate the data from the header
    print('-' * 35)
    # Requesting the student number
    option = int(input('Show grades of which student? (999 to stop): '))
    # If the user types 999, stop the while loop
    if option == 999:
        break
    # If the student number is valid, print the name of the student and the grades
    if option <= len(students) - 1:
        print(f'Grades of {students[option][0]} are {students[option][1]}')
# Printing a message to indicate the end of the program
print('FINISH')