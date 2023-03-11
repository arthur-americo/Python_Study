''' Reads the name, age and gender of 4 people and shows the average age of the group, 
the name of the oldest man and how many women are under 20 years old:
total_age = 0'''

# Initialize variables to keep track of total age, oldest man and women under 20
total_age = 0
oldest_man_age = 0
oldest_man_name = ""
women_under_20 = 0

# Loop over 4 people
for i in range(1, 5):
    print(f"Person {i}")
    # Get name, age and gender from user input
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender (M/F): ")

    # Add age to total_age for calculating average later
    total_age += age

    # Check if person is male and older than current oldest man
    if gender == "M" and age > oldest_man_age:
        # Update oldest man information
        oldest_man_age = age
        oldest_man_name = name

    # Check if person is female and under 20 years old
    if gender == "F" and age < 20:
        # Increment women_under_20 counter
        women_under_20 += 1

# Calculate average age by dividing total_age by number of people (4)
average_age = total_age / 4

# Print results
print(f"The average age of the group is {average_age:.2f}.")
if oldest_man_name:
    print(f"The oldest man is {oldest_man_name}.")
else:
    print("There are no men in the group.")
print(f"There are {women_under_20} women under 20 years old.")