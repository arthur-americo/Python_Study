'''Make a program that has a function called bigger(), which receives several parameters with integer values.
Your program has to look at all the values and say which one is the largest.'''
def bigger(*args):
    max_value = args[0]
    for value in args:
        if value > max_value:
            max_value = value
    return max_value

# Main program
numbers = []
while True:
    user_input = input('Enter a number (or "stop" to finish): ')
    if user_input == 'stop':
        break
    else:
        numbers.append(int(user_input))

print(f'The largest number entered is: {bigger(*numbers)}')