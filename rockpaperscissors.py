#!/usr/local/bin/python3

# Example Python program to play the rock, paper, scissors game
#
# Sample output:
#
# ./rockpaperscissors.py
# Player 1 choose rock, paper or scissors? rock
# Player 2 choose rock, paper or scissors? paper
# Player 2 wins because paper covers rock
#
# ./rockpaperscissors.py
# Player 1 choose rock, paper or scissors? paper
# Player 2 choose rock, paper or scissors? rock
# Player 1 wins because paper covers rock
#
# ./rockpaperscissors.py
# Player 1 choose rock, paper or scissors? scissors
# Player 2 choose rock, paper or scissors? rock
# Player 2 wins because rock smashes scissors
#
# ./rockpaperscissors.py
# Player 1 choose rock, paper or scissors? rock
# Player 2 choose rock, paper or scissors? scissors
# Player 1 wins because rock smashes scissors
#
# ./rockpaperscissors.py
# Player 1 choose rock, paper or scissors? scissors
# Player 2 choose rock, paper or scissors? paper
# Player 1 wins because scissors cuts paper
#
# ./rockpaperscissors.py
# Player 1 choose rock, paper or scissors? paper
# Player 2 choose rock, paper or scissors? scissors
# Player 2 wins because scissors cuts paper
#
# ./rockpaperscissors.py
# Player 1 choose rock, paper or scissors? rock
# Player 2 choose rock, paper or scissors? rock
# Player 1 ties with player 2. They both played rock
#
# ./rockpaperscissors.py
# Player 1 choose rock, paper or scissors? scissors
# Player 2 choose rock, paper or scissors? scissors
# Player 1 ties with player 2. They both played scissors
#
# ./rockpaperscissors.py
# Player 1 choose rock, paper or scissors? paper
# Player 2 choose rock, paper or scissors? paper
# Player 1 ties with player 2. They both played paper


import sys
if sys.version_info[0] < 3:
	raise Exception("Must be using python 3")
    
valid_choices = {'rock', 'paper', 'scissors'}  # create a python set of all possible valid choices

def getPlayerInput(player):
    response = input(str(player)+' choose rock, paper or scissors? ')
    response = response.strip().lower()    # strip out whitespace and convert to lowercase
    while response not in valid_choices:
        response = input(str(player)+' choose rock, paper or scissors? ')
        response = response.strip().lower()    # strip out whitespace and convert to lowercase
    return response
    
player1 = getPlayerInput('Player 1')
player2 = getPlayerInput('Player 2')

if player1 == 'rock' and player2 == 'scissors':
    print("Player 1 wins because rock smashes scissors")
elif player1 == 'scissors' and player2 == 'rock':
    print("Player 2 wins because rock smashes scissors")
elif player1 == 'paper' and player2 == 'rock':
    print("Player 1 wins because paper covers rock")
elif player1 == 'rock' and player2 == 'paper':
    print("Player 2 wins because paper covers rock")
elif player1 == 'scissors' and player2 == 'paper':
    print("Player 1 wins because scissors cuts paper")
elif player1 == 'paper' and player2 == 'scissors':
    print("Player 2 wins because scissors cuts paper")
else:
    print("Player 1 ties with player 2. They both played "+player1)
