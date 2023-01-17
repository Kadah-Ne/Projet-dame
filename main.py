import tkinter as tk

class Jeu :
    def __init__(self,board,ia,action) -> None:
        self.fenetre = tk.Tk()
        self.TargetStart = None
        self.TargetEnd = None
        self.board = board
        self.ia = ia
        self.action = action
        self.player = 0

        self.canvas = tk.Canvas(self.fenetre, width=600, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.pion_clique)

        self.dessinePlateau()
        self.dessinePions(board.Board)
        self.jouer()
        
        
    def dessinePlateau(self):
        self.fenetre.title("Jeu de dames")
        for i in range(10):
            for j in range(10):
                couleur = "white" if (i + j) % 2 == 0 else "lightgrey"
                x1, y1 = i * 50, j * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
    
    def dessinePions(self,board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != None and board[i][j][0] == 1:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="black")
                elif board[i][j] != None and board[i][j][0] == 0:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="white")

    def pion_clique(self,event):
        # Récupérer les coordonnées du clic de la souris
        x, y = event.x, event.y
        # Calculer la ligne et la colonne du pion sélectionné
        ligne = x // 50
        colonne = y // 50
        # Afficher les coordonnées du pion sélectionné
        print(f"Pion sélectionné : ligne {ligne}, colonne {colonne}")
        if self.TargetStart == None:
            self.TargetStart = str(ligne)+str(colonne)
        elif self.TargetEnd == None:
            self.TargetEnd = str(ligne)+str(colonne)

    def jouer(self):
        #while True:
        self.board.convertIA()
        self.board.printBoard(board.IABoard)
        movement = False
        while not movement :
            move = ""
            while self.TargetStart==None and self.TargetEnd==None:
                print(f"Votre action Joueur {self.player} : \n")
            move = (self.TargetStart+","+self.TargetEnd)
            startPos,endPos = move.split(",")
            startPos = int(startPos)
            endPos = int(endPos)
            movement = self.action.movement(board.Board,startPos,endPos,player)

        print("--------------------------------")
        if self.player == 0:
            self.board.convertIA() 
            print(self.ia.play(plateau = self.board.IABoard,premier_joueur=False))
            self.player = 1
        else:
            self.player = 0
        
        self.fenetre
    

    
    















from damier import damier
from actions import *
from Graphic import *
from ia import ia

g = graph()
board = damier()
Bot = ia()
a = actions()
dames = Jeu(board,Bot,a)

# player = 0
# g.dessinePlateau()
# g.dessinePions()
# while a.Playable:
#     board.convertIA()
#     board.printBoard(board.IABoard)
#     movement = False
#     while not movement :
#         move = ""
#         while not move.__contains__(","):
#             move = input(f"Votre action Joueur {player} : \n")
#         startPos,endPos = move.split(",")
#         startPos = int(startPos)
#         endPos = int(endPos)
#         movement = a.movement(board.Board,startPos,endPos,player)

#     print("--------------------------------")
#     if player == 0:
#         board.convertIA() 
#         print(Bot.play(plateau = board.IABoard,premier_joueur=False))
#         player = 1
#     else:
#         player = 0


