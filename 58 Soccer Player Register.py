'''Create a program that manages the performance of a football player. 
The program will read the player's name and how many games he played. 
Then you will read the number of goals scored in each match. In the end, all of this will be stored in a dictionary, 
including the total number of goals scored during the championship.'''
players = []

while True:
    player = {}
    goals = []

    player['name'] = input('Player name: ')
    matches = int(input(f'How many matches did {player["name"]} play? '))

    for match in range(matches):
        goals.append(int(input(f'How many goals in match {match+1}? ')))

    player['goals'] = goals
    player['total'] = sum(goals)
    
    players.append(player)

    continue_registering = input('Continue registering? [Y/N] ').upper()
    if continue_registering == 'N':
        break

print('Players:')
for player in players:
    print(f'{player["name"]}: {player["total"]} goals')

while True:
    view_details = input('View details of a player? [Y/N] ').upper()
    
    if view_details == 'N':
        break
    
    player_name = input('Player name: ')
    
    for player in players:
        if player['name'] == player_name:
            print(f'{player["name"]}:')
            for index, goal in enumerate(player['goals']):
                print(f'Match {index+1}: {goal} goals')
            break