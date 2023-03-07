'''Create a program that has a function called Vote () that will receive as a parameter the year of birth of a person, 
returning a literal value indicating if a person has a vote, optional and mandatory in the elections.'''
# This function receives the user's birth year as a parameter
def vote(birth_year):
    # Defining the current year
    from datetime import date
    current_year = date.today().year
    # Calculating the user's age
    age = current_year - birth_year
    # Conditional structure to return the user's voting status
    if age < 16:
        return 'Vote not allowed'
    elif 16 <= age < 18 or age > 70:
        return 'Optional vote'
    else:
        return 'Mandatory vote'
# Requesting the user's birth year
birth_year = int(input('Enter your birth year: '))
# Printing the user's voting status
print(vote(birth_year))

