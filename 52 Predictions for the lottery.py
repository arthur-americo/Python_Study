'''Make a program that helps a lottery player to create guesses. 
The program will ask how many games will be generated and will raffle 6 numbers between 1 and 60 for each game, 
registering everything in a composite list.'''
# import the sample function from the random module
from random import sample
# create a list to store the games
games = []
# get the number of games from the user
num_games = int(input('How many games do you want to generate? '))
# loop through the number of games
for i in range(num_games):
    # generate a list of 6 random numbers from 1 to 60
    # append the list to the games list
    games.append(sample(range(1, 61), 6))
# loop through the games and print them out
for i, game in enumerate(games):
    print(f'Game {i+1}: {game}')