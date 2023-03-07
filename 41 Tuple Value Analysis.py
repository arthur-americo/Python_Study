'''Develop a program that reads four values from the keyboard and stores them in a tuple. At the end, show:

A) How many times did the value 9 appear.

B) In which position was entered the first value 3.

C) What were the even numbers.'''

numbers = (int(input('Enter a number: ')),
           int(input('Enter a number: ')),
           int(input('Enter a number: ')),
           int(input('Enter a number: ')))

print(f'The value 9 appears {numbers.count(9)} times.')

if 3 in numbers:
    print(f'The value 3 first appears at position {numbers.index(3) + 1}.')
else:
    print('The value 3 was not entered.')

print('The even values entered were:', end=' ')
for number in numbers:
    if number % 2 == 0:
        print(number, end=' ')

