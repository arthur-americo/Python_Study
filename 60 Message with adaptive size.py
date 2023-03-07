'''Write a program that has a function called write(), which takes any text as a parameter and displays a message
with an adaptable size.'''
def write(text):
    length = len(text)
    print('-' * (length + 4))
    print('|' + text + '|')
    print('-' * (length + 4))

#user input in using the function
n = input('Enter a text: ')
print(write(n))