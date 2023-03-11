'''Python program that shows the multiplication table of several numbers, one at a time, for each value entered by the user. 
The program will be interrupted when the requested number is negative:'''
while True:
    # Get number from user input
    num = int(input("Enter a number: "))

    # Check if number is negative
    if num < 0:
        break

    # Print multiplication table using for loop
    for i in range(1, 11):
        result = num * i
        print(f"{num} x {i} = {result}")

    print()