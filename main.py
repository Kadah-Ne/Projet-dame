from damier import damier
from actions import *
from ia import ia
board = damier()
Bot = ia()
a = actions()
player = 0

while a.Playable:    
    board.printBoardT()
    startPos,endPos = input(f"Votre action Joueur {player} : \n").split(",")
    startPos = int(startPos)
    endPos = int(endPos)
    a.movement(board.Board,startPos,endPos,player)
    board.convertIA()
    print("--------------------------------")
    if player == 0:
        print(Bot.play(plateau = board.IABoard,premier_joueur=False))
        player = 1
    else:
        player = 0


