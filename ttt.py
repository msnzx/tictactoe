import sys
from tttlib import playGame, humanMove
from tttai import randomBotMove

if len(sys.argv) != 3:
    print("Usage: python ttt.py <player1> <player2>")
    print("Valid players: 'h' for human, 'r' for randomBot")
    sys.exit(1)

player1, player2 = sys.argv[1], sys.argv[2]

if player1 == 'h':
    player1 = humanMove
elif player1 == 'r':
    player1 = randomBotMove

if player2 == 'h':
    player2 = humanMove
elif player2 == 'r':
    player2 = randomBotMove

playGame(player1, player2)