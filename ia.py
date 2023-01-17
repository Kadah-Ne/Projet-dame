from random import *
from damier import *
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
        
        listeMove.append(caseDep+MoveR)
        listeMove.append(caseDep+MoveL)
        
        if self.board[caseDep+MoveL] != None:
            listeMove.append(caseDep+EatL)
        if self.board[caseDep+MoveR] != None:
            listeMove.append(caseDep+EatR)

        return listeMove[randint(0,len(listeMove)-1)]
            
                
    def estJouable(self,ListePion,Player):
        # dam = damier()
        # dam.printBoard()
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
            if self.board[i+MoveR] == None or self.board[i+MoveL] == None:
                if i%10 == 0 and self.board[i+MoveR] != None:
                    continue
                elif str(i)[-1] == "9" and self.board[i+MoveL] != None:
                    continue

                self.listeJouable.append(i)
            elif (self.board[i+MoveR][0] != idPlayer) and (self.board[i+EatR] == None):
                if (i%10 == 0 or str(i)[-1] == "1" ) and self.board[i+EatR] != None:
                    continue
                self.listeJouable.append(i)  

            elif (self.board[i+MoveL][0] !=idPlayer)  and (self.board[i+EatL] == None)  :
                if str(i)[-1] == ("9" or "8") and self.board[i+EatL] != None:
                    continue
                self.listeJouable.append(i)  
                
        