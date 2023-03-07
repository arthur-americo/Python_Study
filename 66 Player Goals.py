'''Make a program that has a function called form (), which receives two optional parameters: 
the name of a player and how many goals he scored. The program should be able to show the player's record, 
even if any data has not been reported correctly.'''
def form():
    # Initialize an empty dictionary to hold the player data.
    players = {}

    # Keep looping until the user enters "q".
    while True:
        # Prompt the user to enter a player name.
        player = input('Enter player name (or "q" to quit): ')

        # If the user entered "q", break out of the loop.
        if player == 'q':
            break

        # Prompt the user to enter the number of goals.
        goals = input('Enter number of goals: ')

        # Try to convert the number of goals to an integer. If it fails, set the number of goals to 0.
        try:
            goals = int(goals)
        except ValueError:
            goals = 0

        # Add the player name and the number of goals to the dictionary.
        players[player] = goals

    # Loop through the players dictionary, printing the player name and the number of goals.
    for player, goals in players.items():
        print(f'Player: {player}')
        print(f'Goals: {goals}')

form()