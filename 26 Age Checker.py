
# reads the birth year of seven people and shows how many have not yet reached the age of majority and how many are already adults
from datetime import date

current_year = date.today().year
adults = 0
minors = 0

for i in range(1, 8):
    birth_year = int(input(f"Enter the birth year of person {i}: "))
    age = current_year - birth_year
    if age >= 18:
        adults += 1
    else:
        minors += 1

print(f"{adults} people are adSSults.")
print(f"{minors} people are minors.")