'''Write a program that makes the computer "think" of an integer between 0 and 5 and ask the user to try
find out which number was chosen by the computer. The program should write on the screen if the user won or lost.'''
import random

secret_number = random.randint(0, 5)
guess = int(input('Try to guess the number the computer chose between 0 and 5: '))

if guess == secret_number:
    print('Congratulations! You got it right!')
else:
    print(f'You missed it! The number chosen by the computer was {secret_number}.')