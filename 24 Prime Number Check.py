# Get user input
num = int(input("Enter a number: "))

# Check if the number is less than or equal to 1
if num <= 1:
    print(num, "is not a prime number.")
else:
    # Assume the number is prime until proven otherwise
    is_prime = True

    # Check if the number has any factors other than 1 and itself
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    # Print the result
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")