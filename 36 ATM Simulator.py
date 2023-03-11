'''Python program that simulates the operation of an ATM. At the beginning, it asks the user for the amount to be withdrawn 
(an integer) and the program will inform how many banknotes of each value will be delivered. Note that the ATM has banknotes 
of R$50, R$20, R$10 and R$1'''
# Get amount to withdraw from user input
amount = int(input("Enter the amount to withdraw: "))

# Initialize variables to keep track of number of banknotes
fifties = twenties = tens = ones = 0

# Calculate number of banknotes for each value
if amount >= 50:
    fifties = amount // 50
    amount %= 50

if amount >= 20:
    twenties = amount // 20
    amount %= 20

if amount >= 10:
    tens = amount // 10
    amount %= 10

ones = amount

# Print results
print(f"You will receive:")
if fifties > 0:
    print(f"{fifties} banknote(s) of R$50")
if twenties > 0:
    print(f"{twenties} banknote(s) of R$20")
if tens > 0:
    print(f"{tens} banknote(s) of R$10")
if ones > 0:
    print(f"{ones} banknote(s) of R$1")