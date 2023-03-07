'''Python exercise 074: Create a program that will generate five random numbers and put them in a tuple. After that,
show the list of generated numbers and also indicate the smallest and largest values in the tuple.'''
import random

def random_numbers():
    numbers = tuple(random.randint(0, 10) for _ in range(5))
    return numbers

numbers_tuple = random_numbers()
print(f"The number are: {numbers_tuple}")
print(f"The lowest value is {min(numbers_tuple)}")
print(f"The highest value is {max(numbers_tuple)}")
