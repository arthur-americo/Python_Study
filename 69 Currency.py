'''Create a module called currency.py that has the functions incorporated to 
increase (), decrease (), double () and half ().'''

#Increase the given value by the given percentage.
def increase(value, percentage):
    return value + (value * percentage / 100)

#Returns the given value decreased by the given percentage.
def decrease(value, percentage):
    return value - (value * percentage / 100)

#Returns double the given value.
def double(value):
    return value * 2

#Returns half the given value.
def half(value):
    return value / 2
   
#Returns the square of the given value.
def square(value):
    return value ** 2

# Returns the cube of the given value.
def cube(value):
    return value ** 3

#Returns the square root of the given value.
def root(value):
    return value ** (1/2)

#  Returns the given value as a formatted currency string.
def currency(value, symbol='$', decimal_places=2):
    formatted_value = f"{symbol}{value:,.{decimal_places}f}"
    return formatted_value

  #Prints a summary of the given value.
def summary(value, symbol='$', decimal_places=2):
    print(f'Original Value: {currency(value, symbol=symbol, decimal_places=decimal_places)}')
    print(f'Double: {currency(double(value), symbol=symbol, decimal_places=decimal_places)}')
    print(f'Half: {currency(half(value), symbol=symbol, decimal_places=decimal_places)}')

def help():
    print('Available functions:')
    print('increase(value, percentage) - Increases the given value by the given percentage.')
    print('decrease(value, percentage) - Decreases the given value by the given percentage.')
    print('double(value) - Doubles the given value.')
    print('half(value) - Halves the given value.')
#how to use
'''You can name this code currency.py since it's a Python module that contains functions for working with currency values. 
To use this module in your own code, you would save it to a file named currency.py in the same directory as your main script 
and then import it using the import statement like this:
import currency

value = 1234.5678
formatted_value = currency.currency(value)
print(formatted_value) # prints $1,234.57

You can also specify a different currency symbol and number of decimal places if you wish:
import currency

value = 1234.5678
formatted_value = currency.currency(value, symbol='€', decimal_places=3)
print(formatted_value) # prints €1,234.568

'''