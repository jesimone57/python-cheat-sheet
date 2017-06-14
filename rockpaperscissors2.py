#!/usr/local/bin/python3

# Example Python program to play the rock, paper, scissors game

# ./rockpaperscissors2.py
# Player 1 choose rock, paper or scissors? scissors
# Player 1 chooses scissors
# Player 2 choose rock, paper or scissors? paper
# Player 2 chooses paper
# scissors wins over paper  Player 1 wins.

# ./rockpaperscissors2.py
# Player 1 choose rock, paper or scissors? scissors
# Player 1 chooses scissors
# Player 2 choose rock, paper or scissors? rock
# Player 2 chooses rock
# rock wins over scissors  Player 2 wins.

# ./rockpaperscissors2.py
# Player 1 choose rock, paper or scissors? rock
# Player 1 chooses rock
# Player 2 choose rock, paper or scissors? paper
# Player 2 chooses paper
# paper wins over rock  Player 2 wins.

import sys
if sys.version_info[0] < 3:
	raise Exception("Must be using python 3")

def getPlayerInput(player):
    response = ''
    while response not in {'rock', 'paper', 'scissors'}:
        response = input(str(player)+' choose rock, paper or scissors? ')
        response = response.strip().lower()    # strip out whitespace and convert to lowercase
    return response
    
response1 = getPlayerInput('Player 1')
print('Player 1 chooses '+str(response1))
response2 = getPlayerInput('Player 2')
print('Player 2 chooses '+str(response2))

winning_combinations = {('rock','scissors'), ('scissors', 'paper'), ('paper','rock')}
if (response1, response2) in winning_combinations:
    print(str(response1)+" wins over "+str(response2)+"  Player 1 wins.")
elif (response2, response1) in winning_combinations:
    print(str(response2)+" wins over "+str(response1)+"  Player 2 wins.")
else:
    print("It's a tie. Player 1 and 2 both played "+response1)
