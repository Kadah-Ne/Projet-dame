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

        self.canvas = tk.Canvas(self.fenetre, width=520, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.pion_clique)

        self.dessinePlateau("")
        self.dessinePions(self.board.Board)
        self.fenetre.mainloop()

    def checkWin(self,board):
        listePionsB = 0
        listePionsN = 0
        for i in board:
            if i != None:
                if i[0] == 0:
                    listePionsB +=1
                else:
                    listePionsN +=1
        if listePionsB == 0 :
            return "Noir"
        elif listePionsN == 0 :
            return "Blanc"
        else:
            return None
            
    def writeMessage(self,Message):
        self.dessinePlateau()
        self.canvas.create_text((260, 570),text=f"Information : {Message}",fill="Black",font='tkDefaeultFont 12')
        self.dessinePions(board.Board)
        
    def dessinePlateau(self,IaPlays = None):
        self.canvas.delete("all")
        self.fenetre.title("Jeu de dames")
        self.canvas.create_text((260, 550),text=f"Move de l'IA : {IaPlays}",fill="Black",font='tkDefaeultFont 12')
        cpt = 0
        for i in range(10):
            for j in range(10):
                couleur = "white" if (i + j) % 2 == 0 else "lightgrey"
                x1, y1 = i * 50, j * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
                
                cpt+=1
    
    def dessinePions(self,board, selectX = None,selectY =None, player = None):
        cptX,cptY=0,0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if selectX != None and selectY != None and j == selectX and i == selectY and board[i][j][0] == player:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="Red")
                elif board[i][j] != None and board[i][j][0] == 1 and board[i][j][1] == False:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="black")
                elif board[i][j] != None and board[i][j][0] == 0 and board[i][j][1] == False:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="white")
                elif board[i][j] != None and board[i][j][0] == 0 and board[i][j][1] == True:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="white")
                    self.canvas.create_text((j*50+10,i*50+10),text="Q", fill="Black",font='tkDefaeultFont 12')
                elif board[i][j] != None and board[i][j][0] == 1 and board[i][j][1] == True:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="black")
                    self.canvas.create_text((j*50+10,i*50+10),text="Q", fill="black",font='tkDefaeultFont 12')
                if i == len(board)-1:
                    self.canvas.create_text(j*50+25,i*50 + 60,text=f"{cptY}",fill="Black",font='tkDefaeultFont 12')
                    cptY += 1
            self.canvas.create_text(j*50+60,i*50+25,text=f"{cptX}",fill="Black",font='tkDefaeultFont 12')
            
            cptX +=1 
                    

    def pion_clique(self,event):
        # Récupérer les coordonnées du clic de la souris
        x, y = event.x, event.y
        # Calculer la ligne et la colonne du pion sélectionné
        ligne = x // 50
        colonne = y // 50
        # Afficher les coordonnées du pion sélectionné
        if self.TargetStart == None:
            if board.Board[colonne][ligne][0] == self.player :
                self.TargetStart = str(colonne)+str(ligne)
                self.dessinePlateau()
                self.dessinePions(self.board.Board,ligne,colonne,self.player)
            else:
                self.writeMessage(Message=f"Ce n'est pas votre Pion joueur {self.player}")
                
            
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

                self.dessinePlateau(IaPlays)
                self.dessinePions(self.board.Board)
                self.winner = self.checkWin(self.board.IABoard)
                if self.winner != None:
                    self.writeMessage(f"{self.winner} wins")
                    quit()
            else :
                print(f"Action Interdite Joueur {self.player}")
            self.move = ""


dames = Jeu(board,Bot,a)




