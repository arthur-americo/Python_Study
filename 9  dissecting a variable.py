#dissecting a variable
# Ask the user to type something
n= float(input('Type something: '))

# Inform the user what was typed
print('The primitive type of this value is ', type(n))

# Inform the user if there are spaces in the input
print('Are there spaces? ', n.isspace())