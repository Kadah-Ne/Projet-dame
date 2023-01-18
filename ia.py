from random import *

class ia:
    def __init__(self) -> None:
        self.board = []
        self.listeJouable = []

        pass
    
    def play(self,plateau : list,premier_joueur : bool) -> tuple:
        listePions = []
        self.board = plateau
        if premier_joueur :
            Player = 0
        else :
            Player = 1
        self.estJouable(self.listingPawn(premier_joueur),Player)
        print(self.listeJouable)
        # caseDep = self.listeJouable[randint(0,len(self.listeJouable)-1)]
        # caseFin = self.choixMove(caseDep,premier_joueur)
        # return(caseDep,caseFin)


    def listingPawn(self,Player) -> list[int]:
        listePions = []
        cpt = 0
        for i in self.board:
            if i != None:
                player= i[0]
                if Player and player == 0:
                    listePions.append(cpt)
                elif not Player and player == 1:
                    listePions.append(cpt)
            cpt+=1
        return listePions

    
    def estJouable(self,ListePion,Player):
        MoveR,MoveL,EatR,EatL = self.associationPlayer(Player)
        for i in ListePion:
            if self.checkMove(self.board,i,i+MoveL,Player) :
                self.listeJouable.append(i)
            elif self.checkMove(self.board,i,i+MoveR,Player) :
                self.listeJouable.append(i)
            elif self.checkMove(self.board,i,i+EatL,Player) :
                self.listeJouable.append(i)
            elif self.checkMove(self.board,i,i+EatR,Player):
                self.listeJouable.append(i)
                

    def associationPlayer(self,turnPlayer) -> tuple():
        if not turnPlayer :
            return(-9,-11,-18,-22)
        else:
            return(11,9,22,18)
        
    def checkMove(self,board,startPos,endPos,turnPlayer) -> bool:
        
        MoveR,MoveL,EatR,EatL = self.associationPlayer(turnPlayer)

        if board[startPos] != None and board[startPos][0] == turnPlayer:
            spacesToMove = endPos - startPos
            if spacesToMove == MoveL or spacesToMove == MoveR or spacesToMove == EatL or spacesToMove == EatR:
                if str(startPos)[-1] == "0" and spacesToMove == MoveL:
                    return False
                elif str(startPos)[-1] == "9" and spacesToMove == MoveR:
                    return False
                elif (str(startPos)[-1] == "0" or str(startPos)[-1] == "1" )and spacesToMove == EatL:
                    return False
                elif (str(startPos)[-1] == "9" or str(startPos)[-1] == "8" ) and spacesToMove == EatR:
                    return False
                
                match spacesToMove:
                    case (9 | -9 | 11 | -11):
                        if board[endPos] == None:
                            return True
                        else :
                            return False
                    case (18 | -18 | 22 | -22):
                        middlePos = startPos + int(spacesToMove/2)
                        if board[middlePos][0] != turnPlayer:
                            return True
                        else:
                            return False
            else :
                return False
        else :
            return False

    def choixMove(self,caseDep,Player):
        listeMove = []
        

        
            
                
    
            