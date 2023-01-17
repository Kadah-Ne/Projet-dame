from random import *

class ia:
    def __init__(self) -> None:
        self.board = []
        self.listeJouable = []

        pass
    
    def play(self,plateau : list,premier_joueur : bool) -> tuple:
        
        listePions = []
        self.board = plateau
        cpt = 0
        for i in plateau:
            if i != None:
                player,isQueen = i
                if premier_joueur and player == 0:
                    listePions.append(cpt)
                elif not premier_joueur and player == 1:
                    listePions.append(cpt)
            cpt+=1
        self.estJouable(listePions,premier_joueur)
        caseDep = self.listeJouable[randint(0,len(self.listeJouable)-1)]
        caseFin = self.choixMove(caseDep,premier_joueur)
        return(caseDep,caseFin)
        
    def choixMove(self,caseDep,Player):
        listeMove = []
        if Player :
            idPlayer = 0
            MoveR = -9
            MoveL = -11
            EatR = -18
            EatL = -22
        else :
            idPlayer =1
            MoveR = 11
            MoveL = 9
            EatR = 22
            EatL = 18
        
        if self.board[caseDep+MoveL] == None and (str(caseDep)[-1] != "0" and str(caseDep+MoveL)[-1] !="9"):
            listeMove.append(caseDep+MoveL)
        if self.board[caseDep+MoveR] == None and (str(caseDep)[-1] != "9" and str(caseDep+MoveL)[-1] !="0"):
            listeMove.append(caseDep+MoveR)
        if self.board[caseDep+MoveL] != None and self.board[caseDep+MoveL][0] != idPlayer:
            listeMove.append(caseDep+EatL)
        if self.board[caseDep+MoveR] != None and self.board[caseDep+MoveR][0] != idPlayer:
            listeMove.append(caseDep+EatR)



        if len(listeMove) != 0:
            return listeMove[randint(0,len(listeMove)-1)]
        else :
            print("Erreur, aucun move jouable")
            
                
    def estJouable(self,ListePion,Player):
        if Player :
            idPlayer = 0
            MoveR = -9
            MoveL = -11
            EatR = -18
            EatL = -22
        else :
            idPlayer = 1
            MoveR = 11
            MoveL = 9
            EatR = 22
            EatL = 18
        for i in ListePion:
            #PionAvance
            if self.board[i+MoveR] == None or self.board[i+MoveL] == None:
                if i%10 == 0 and self.board[i+MoveR] != None:
                    continue
                elif str(i)[-1] == "9" and self.board[i+MoveL] != None:
                    continue
                self.listeJouable.append(i)
            #PionMangeDroite
            elif (self.board[i+MoveR][0] != idPlayer) and (self.board[i+EatR] == None):
                if (i%10 == 0 or str(i)[-1] == "1" ) and self.board[i+EatR] != None:
                    continue
                self.listeJouable.append(i)  

            #PionMangeGauche
            elif (self.board[i+MoveL][0] !=idPlayer) and (self.board[i+EatL] == None)  :
                if str(i)[-1] == ("9" or "8") and self.board[i+EatL] != None:
                    continue
                self.listeJouable.append(i)

            #Dame Recule  
            elif self.board[i][1] and (self.board[i-MoveL][0] == None) or (self.board[i-MoveR] == None):
                if i%10 == 0 and self.board[i-MoveL] != None:
                    continue
                elif str(i)[-1] == "9" and self.board[i-MoveR] != None:
                    continue
                self.listeJouable.append(i)
            
            #Dame MangeDroiteArr
            elif self.board[i][1] and (self.board[i-MoveL][0] !=idPlayer) and (self.board[i-EatL] == None)  :
                if str(i)[-1] == ("9" or "8") and self.board[i-EatL] != None:
                    continue
                self.listeJouable.append(i)
            
            #Dame MangeGaucheArr
            elif self.board[i][1] and (self.board[i-MoveR][0] != idPlayer) and (self.board[i-EatR] == None):
                if (i%10 == 0 or str(i)[-1] == "1" ) and self.board[i-EatR] != None:
                    continue
                self.listeJouable.append(i)  