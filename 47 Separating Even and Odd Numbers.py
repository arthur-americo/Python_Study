'''Create a program that will read several numbers and put them in a list. 
After that, create two extra lists that will contain only the even and odd values entered, respectively. 
At the end, show the contents of the three generated lists.'''
import random

# Create an empty list
list = []

# Append 10 random numbers to list from 0 to 50
while len(list) < 10:
    list.append(random.randint(0, 50))

# Create empty lists for even and odd numbers
even = []
odd = []

# Separate even and odd numbers in list
for num in list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
# Print the lists with different colors
print('\033[31mOriginal list:\033[0m', list)
print('\033[34mEven list:\033[0m', even)
print('\033[33mOdd list:\033[0m', odd)
