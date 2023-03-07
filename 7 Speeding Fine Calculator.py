'''#Write a program that reads the speed of a car. If it exceeds 80 km/h, show a message saying that it has been
fined. The fine will cost R$7.00 for each km over the limit.'''
# Get the speed of the car
speed = float(input('Enter the speed of the car (in km/h): '))

# Check if the speed is greater than 80km/h
if speed > 80:
    # Calculate the fine
    fine = (speed - 80) * 7
    # Print the fine
    print(f'You have been fined R${fine:.2f} for exceeding the speed limit.')
else:
    # Print that the speed is within the limit
    print('You are within the speed limit.')