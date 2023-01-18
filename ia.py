from random import *

class ia:
    def __init__(self) -> None:
        self.board = []
        self.listeJouable = []
        self.pointEat = 3
        self.pointMove = 2

        pass
    
    def play(self,plateau : list,premier_joueur : bool) -> tuple:
        listePions = []
        self.board = plateau
        if premier_joueur :
            Player = 0
        else :
            Player = 1
        self.estJouable(self.listingPawn(premier_joueur),Player)
        pos,move = self.calculPoints(self.listeJouable,self.board,Player)
        return(pos,pos+move)


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
                        if board[middlePos] != None and board[middlePos][0] != turnPlayer and board[startPos+spacesToMove] == None:
                            return True
                        else:
                            return False
            else :
                return False
        else :
            return False

    def checkDanger(self,board,postion,player,origin):
        MoveR,MoveL = self.associationPlayer(player)[0],self.associationPlayer(player)[1]
        dangerLevel = 0
        if board[postion+MoveR] != None and board[postion+MoveR][0] != player and (board[postion-MoveR] == None or (postion - MoveR == origin)):
            dangerLevel += 1
        if board[postion+MoveL] != None and board[postion+MoveL][0] != player and (board[postion-MoveL] == None or (postion - MoveL == origin)) :
            dangerLevel += 1
        if board[postion-MoveR] != None and board[postion-MoveR][0] != player and board[postion-MoveR][1] and (board[postion+MoveL] == None or (postion + MoveR == origin)):
            dangerLevel += 1
        if board[postion-MoveL] != None and board[postion-MoveL][0] != player and board[postion-MoveL][1] and (board[postion+MoveR] == None or (postion - MoveR == origin)):
            dangerLevel += 1
        return dangerLevel

        

    def calculPoints(self,listeJouable, board,turnPlayer):
        
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

            if dicoMoves[i][1] :
                if str(i+MoveR)[0] == "9" or str(i+MoveR)[0] == "0":
                    microListPoints[1] +=self.pointMove*2
                else :
                    microListPoints[1] +=self.pointMove
                microListPoints[1] -= self.checkDanger(board,i+MoveR,turnPlayer,i)

            if dicoMoves[i][2]:
                if str(i+EatL)[0] == "9" or str(i+EatL)[0] == "0":
                    microListPoints[2] +=self.pointEat*2
                else :
                    microListPoints[2] +=self.pointEat
                microListPoints[2] -= self.checkDanger(board,i+EatL,turnPlayer,i)

            if dicoMoves[i][3]:
                if str(i+EatR)[0] == "9" or str(i+EatR)[0] == "0":
                    microListPoints[3] +=self.pointEat*2
                else :
                    microListPoints[3] +=self.pointEat
                microListPoints[3] -= self.checkDanger(board,i+EatR,turnPlayer,i)
            dicoPoints[i] = microListPoints
        #print(dicoPoints)
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

    def choixMove(self,caseDep,Player):
        listeMove = []
        

        
            
                
    
            