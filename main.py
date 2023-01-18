import tkinter as tk
from damier import damier
from actions import *
from ia import ia
board = damier()
Bot = ia()
a = actions()

class Jeu :
    def __init__(self,board,ia,action) -> None:
        self.fenetre = tk.Tk()
        self.TargetStart = None
        self.TargetEnd = None
        self.board = board
        self.ia = ia
        self.action = action
        self.player = 0
        self.move = ""
        self.movement = True

        self.canvas = tk.Canvas(self.fenetre, width=500, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.pion_clique)

        self.dessinePlateau("")
        self.dessinePions(self.board.Board)
        self.fenetre.mainloop()
        
        
    def dessinePlateau(self,IaPlays):
        self.fenetre.title("Jeu de dames")
        self.canvas.create_text((250, 550),text=f"Move de l'IA : {IaPlays}",fill="Black",font='tkDefaeultFont 12')
        for i in range(10):
            for j in range(10):
                couleur = "white" if (i + j) % 2 == 0 else "lightgrey"
                x1, y1 = i * 50, j * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
    
    def dessinePions(self,board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != None and board[i][j][0] == 1 and board[i][j][1] == False:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="black")
                elif board[i][j] != None and board[i][j][0] == 0 and board[i][j][1] == False:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="white")
                elif board[i][j] != None and board[i][j][0] == 0 and board[i][j][1] == True:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="white")
                    self.canvas.create_text((j*50+10,i*50+10),text="Q", fill="Black",font='tkDefaeultFont 12')
                elif board[i][j] != None and board[i][j][0] == 1 and board[i][j][1] == True:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="black")
                    self.canvas.create_text((j*50+10,i*50+10),text="Q", fill="black",font='tkDefaeultFont 12')

    def pion_clique(self,event):
        # Récupérer les coordonnées du clic de la souris
        x, y = event.x, event.y
        # Calculer la ligne et la colonne du pion sélectionné
        ligne = x // 50
        colonne = y // 50
        # Afficher les coordonnées du pion sélectionné
        if self.TargetStart == None:
            self.TargetStart = str(colonne)+str(ligne)
        elif self.TargetEnd == None:
            self.TargetEnd = str(colonne)+str(ligne)

            self.move = self.TargetStart+","+self.TargetEnd
            self.TargetStart=None
            self.TargetEnd = None

        if self.move != "":
            startPos,endPos = self.move.split(",")
            self.movement = self.action.moveToPos(self.board.Board,startPos,endPos,self.player)
            if self.movement != False:
                if self.player == 0:
                    self.board.convertIA() 
                    IaPlays = self.ia.play(plateau = self.board.IABoard,premier_joueur=False)
                    self.player = 1
                else :
                    self.board.convertIA() 
                    self.player = 0
                    IaPlays =""

                self.canvas.delete("all")
                self.dessinePlateau(IaPlays)
                self.dessinePions(self.board.Board)
            else :
                print(f"Action Interdite Joueur {self.player}")
            self.move = ""


dames = Jeu(board,Bot,a)




