'''Create a program where 4 players roll a die and get random results. 
Store these results in a Python dictionary. In the end, put that dictionary in order, 
knowing that the winner got the highest number on the dice.'''
import random

results = {}
for player in range(1, 5):
    results[f'player{player}'] = random.randint(1, 6)

sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

print(sorted_results)