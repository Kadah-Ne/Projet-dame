#Neccessite au moin Python 3.10
from random import *

class ia:
    def __init__(self) -> None:
        self.board = []
        self.listeJouable = []

        #Points de priorités, si pointEat > pointMove -> mange si possible (doit etre suppérieur a 2)
        self.pointEat = 3
        self.pointMove = 2
        pass
    
    #Fonction principale
    def play(self, plateau : list, premier_joueur : bool) -> tuple:
        self.board = plateau
        if premier_joueur :
            Player = 0
        else :
            Player = 1

        #Calcule du prochain mouvement
        self.estJouable(self.listingPawn(premier_joueur),Player)
        pos,move = self.calculPoints(self.listeJouable,self.board,Player)
        return(pos,pos+move)

    #Récupere une liste de toutes les positions des pions de l'IA
    def listingPawn(self, turnPlayer : bool) -> list[int]:
        listePions = []
        cpt = 0
        for i in self.board:
            if i != None:
                player= i[0]
                if turnPlayer and player == 0:
                    listePions.append(cpt)
                elif not turnPlayer and player == 1:
                    listePions.append(cpt)
            cpt+=1
        return listePions

    #Parcour la liste des pions de l'IA et récupere toutes les actions possibles de l'IA
    def estJouable(self, ListePion : list[int], Player:bool) -> None:
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
                
    #Permet de récupérer les variables de movement liée au joueur
    def associationPlayer(self, turnPlayer : bool) -> tuple(int):
        if not turnPlayer :
            return(-9,-11,-18,-22)
        else:
            return(11,9,22,18)

    #Verifie la possibilité d'une action    
    def checkMove(self, board : list[tuple], startPos : int, endPos : int, turnPlayer : bool) -> bool:
        MoveR,MoveL,EatR,EatL = self.associationPlayer(turnPlayer)
        if board[startPos] != None and board[startPos][0] == turnPlayer:
            spacesToMove = endPos - startPos
            #Cas pour un pion lambda
            if 0<spacesToMove+startPos <100:
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
                            if board[middlePos] != None and board[middlePos][0] != turnPlayer and board[startPos+spacesToMove] == None:
                                return True
                            else:
                                return False

                #Cas pour une dame            
                if board[startPos][1]:
                    if turnPlayer ==0 :
                        BackR,BackL,BackEatR,BackEatL = self.associationPlayer(1)
                    else:
                        BackR,BackL,BackEatR,BackEatL = self.associationPlayer(0)
                    if str(startPos)[-1] == "0" and spacesToMove == BackL:
                        return False
                    elif str(startPos)[-1] == "9" and spacesToMove == BackR:
                        return False
                    elif (str(startPos)[-1] == "0" or str(startPos)[-1] == "1" ) and spacesToMove == BackEatL:
                        return False
                    elif (str(startPos)[-1] == "9" or str(startPos)[-1] == "8" ) and spacesToMove == BackEatR:
                        return False
                    
                    match spacesToMove:
                        case (9 | -9 | 11 | -11):
                            if board[endPos] == None:
                                return True
                            else :
                                return False
                        case (18 | -18 | 22 | -22):
                            middlePos = startPos + int(spacesToMove/2)
                            if board[middlePos] != None and board[middlePos][0] != turnPlayer and board[startPos+spacesToMove] == None:
                                return True
                            else:
                                return False
                else :
                    return False
            else :
                return False
        else :
            return False

    #Met un niveau de danger a une action
    def checkDanger(self, board:list[tuple], postion:int, player:bool, origin:int) -> int:
        MoveR,MoveL = self.associationPlayer(player)[0],self.associationPlayer(player)[1]
        dangerLevel = 0
        if (0<=postion+MoveR <=99 or 0<=postion-MoveR <=99) and board[postion+MoveR] != None and board[postion+MoveR][0] != player and (board[postion-MoveR] == None or (postion - MoveR == origin)):
            dangerLevel += 1
        if (0<=postion+MoveL <=99 or 0<=postion-MoveL <=99) and  board[postion+MoveL] != None and board[postion+MoveL][0] != player and (board[postion-MoveL] == None or (postion - MoveL == origin)) :
            dangerLevel += 1
        if (0<=postion+MoveR <=99 or 0<=postion-MoveR <=99) and board[postion-MoveR] != None and board[postion-MoveR][0] != player and board[postion-MoveR][1] and (board[postion+MoveL] == None or (postion + MoveR == origin)):
            dangerLevel += 1
        if (0<=postion+MoveL <=99 or 0<=postion-MoveL <=99) and  board[postion-MoveL] != None and board[postion-MoveL][0] != player and board[postion-MoveL][1] and (board[postion+MoveR] == None or (postion - MoveR == origin)):
            dangerLevel += 1        
        return dangerLevel

    #Met un niveau d'urgence a une action (si une piece risque de se faire manger au prochain tour, essaye en priorité de la sauver)
    def checkUrgency(self, board:list[tuple], postion:int, player:bool) -> int:
        MoveR,MoveL = self.associationPlayer(player)[0],self.associationPlayer(player)[1]
        urgencyLevel = 1

        if (0<=postion+MoveR <=99 or 0<=postion-MoveR <=99) and board[postion+MoveR] != None and board[postion+MoveR][0] != player and (board[postion-MoveR] == None):
            urgencyLevel = 2
        if (0<=postion+MoveL <=99 or 0<=postion-MoveL <=99) and board[postion+MoveL] != None and board[postion+MoveL][0] != player and (board[postion-MoveL] == None) :
            urgencyLevel = 2
        if (0<=postion+MoveR <=99 or 0<=postion-MoveR <=99) and board[postion-MoveR] != None and board[postion-MoveR][0] != player and board[postion-MoveR][1] and (board[postion+MoveL] == None):
            urgencyLevel = 2
        if (0<=postion+MoveL <=99 or 0<=postion-MoveL <=99) and board[postion-MoveL] != None and board[postion-MoveL][0] != player and board[postion-MoveL][1] and (board[postion+MoveR] == None):
            urgencyLevel = 2
        return urgencyLevel

        
    #Pour déterminer la meilleur action, on lui attribut des point selon son niveau de dangerosité, d'urgence, si on mange, si on fais une promotion ect
    def calculPoints(self, listeJouable:list[int], board : list[tuple], turnPlayer : bool) -> tuple:
        MoveR,MoveL,EatR,EatL = self.associationPlayer(turnPlayer)
        dicoMoves = {}

        for i in listeJouable :
            microList = []
            microList.append(self.checkMove(board,i,i+MoveL,turnPlayer))
            microList.append(self.checkMove(board,i,i+MoveR,turnPlayer))
            microList.append(self.checkMove(board,i,i+EatL,turnPlayer))
            microList.append(self.checkMove(board,i,i+EatR,turnPlayer))
            dicoMoves[i] = microList
        dicoPoints = {}
        for i in dicoMoves:
            microListPoints =[0,0,0,0]

            if dicoMoves[i][0] :
                if str(i+MoveL)[0] == "9" or str(i+MoveL)[0] == "0":
                    microListPoints[0] +=self.pointMove*2
                else :
                    microListPoints[0] +=self.pointMove
                microListPoints[0] -= self.checkDanger(board,i+MoveL,turnPlayer,i)
                microListPoints[0] *= self.checkUrgency(board,i,turnPlayer)

            if dicoMoves[i][1] :
                if str(i+MoveR)[0] == "9" or str(i+MoveR)[0] == "0":
                    microListPoints[1] +=self.pointMove*2
                else :
                    microListPoints[1] +=self.pointMove
                microListPoints[1] -= self.checkDanger(board,i+MoveR,turnPlayer,i)
                microListPoints[1] *= self.checkUrgency(board,i,turnPlayer)

            if dicoMoves[i][2]:
                if str(i+EatL)[0] == "9" or str(i+EatL)[0] == "0":
                    microListPoints[2] +=self.pointEat*2
                else :
                    microListPoints[2] +=self.pointEat
                microListPoints[2] -= self.checkDanger(board,i+EatL,turnPlayer,i)
                microListPoints[2] *= self.checkUrgency(board,i,turnPlayer)

            if dicoMoves[i][3]:
                if str(i+EatR)[0] == "9" or str(i+EatR)[0] == "0":
                    microListPoints[3] +=self.pointEat*2
                else :
                    microListPoints[3] +=self.pointEat
                microListPoints[3] -= self.checkDanger(board,i+EatR,turnPlayer,i)
                microListPoints[3] *= self.checkUrgency(board,i,turnPlayer)

            dicoPoints[i] = microListPoints
        dicoChoix={}
        for i in dicoPoints:
            
            bestPoint = max(dicoPoints[i])
            tinyList =[]
            if dicoPoints[i][0] == bestPoint:
                tinyList.append(MoveL)
            if dicoPoints[i][1] == bestPoint:
                tinyList.append(MoveR)
            if dicoPoints[i][2] == bestPoint:
                tinyList.append(EatL)
            if dicoPoints[i][3] == bestPoint:
                tinyList.append(EatR)
            dicoChoix[i] = (bestPoint,choice(tinyList))
        bestOfTheBest = 0
        
        for i in dicoChoix:
            if dicoChoix[i][0] > bestOfTheBest :
                bestOfTheBest = dicoChoix[i][0]
                bestMove = (i,dicoChoix[i][1])
        return bestMove
        

        
            
                
    
            