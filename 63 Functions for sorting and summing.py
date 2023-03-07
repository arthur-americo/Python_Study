'''Write a program that has a list called numbers and two functions called sort() and sumPair(). 
The first function will draw 5 numbers and place them inside the list and the second function will 
show the sum of all the even values drawn by the previous function.'''
from random import randint

def sort():
    numbers = []
    for i in range(5):
        numbers.append(randint(1, 10))
    return numbers

def sumPair(numbers):
    sum = 0
    for number in numbers:
        if number % 2 == 0:
            sum += number
    return sum

numbers = sort()
print(f'The drawn numbers are: {numbers}')
print(f'The sum of the even numbers is: {sumPair(numbers)}')