#!/usr/local/bin/python3

# Example Python program to play the rock, paper, scissors game
#
# Sample output:
#
# ./rockpaperscissors.py 
# Player 1 choose rock, paper or scissors? rock
# Player 1 chooses rock
# Player 2 choose rock, paper or scissors? paper
# Player 2 chooses paper
# Paper covers rock. Player 2 wins
#
# ./rockpaperscissors.py 
# Player 1 choose rock, paper or scissors? rock
# Player 1 chooses rock
# Player 2 choose rock, paper or scissors? rock
# Player 2 chooses rock
# It's a tie. Player 1 and 2 both played rock

import sys
if sys.version_info[0] < 3:
	raise Exception("Must be using python 3")

def getPlayerInput(player):
    response = ''
    while response not in {'rock', 'paper', 'scissors'}:
        response = input(str(player)+' choose rock, paper or scissors? ')
        response = response.strip().lower()    # strip out whitespace and convert to lowercase
    return response
    
player1 = getPlayerInput('Player 1')
print('Player 1 chooses '+str(player1))
player2 = getPlayerInput('Player 2')
print('Player 2 chooses '+str(player2))

if player1 == 'rock' and player2 == 'scissors':
    print("Rock smashes scissors. Player 1 wins.")
elif player1 == 'scissors' and player2 == 'rock':
    print("Rock smashes scissors. Player 2 wins.")
elif player1 == 'paper' and player2 == 'rock':
    print("Paper covers rock.  Player 1 wins.")
elif player1 == 'rock' and player2 == 'paper':
    print("Paper covers rock. Player 2 wins")
elif player1 == 'scissors' and player2 == 'paper':
    print("Scissors cuts paper.  Player 1 wins.")
elif player1 == 'paper' and player2 == 'scissors':
    print("Scissors cuts paper.  Player 2 wins")
else:
    print("It's a tie. Player 1 and 2 both played "+player1)
