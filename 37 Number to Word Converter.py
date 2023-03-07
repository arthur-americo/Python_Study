'''Create a program that has a fully populated pair with a count in words from zero to twenty.
Your program should read a number from the keyboard (between 0 and 20) and display it in full.'''
# Tuple
full = ('zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty')

# Read user input
num = int(input('type a number between 0 and 20: '))

# Verify if the number is between 0 and 20 and print the number in extense
if num >= 0 and num <= 20:
    print(full[num])
else:
    print('Invalid number.Try again.')