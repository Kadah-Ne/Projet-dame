class actions:
    def __init__(self) -> None:
        self.Playable = True
        pass

    def associationPlayer(self,turnPlayer) -> tuple():
        if not turnPlayer :
            return(-9,-11,-18,-22)
        else:
            return(11,9,22,18)


    def checkMove(self,board,startPos,endPos,turnPlayer) -> bool:
        startX,startY = int(startPos[0]),int(startPos[1])
        endX,endY = int(endPos[0]),int(endPos[1])
        MoveR,MoveL,EatR,EatL = self.associationPlayer(turnPlayer)
        

        if board[startX][startY] != None and board[startX][startY][0] == turnPlayer:
            spacesToMove = int(endPos) - int(startPos)
            if spacesToMove == MoveL or spacesToMove == MoveR or spacesToMove == EatL or spacesToMove == EatR:
                if startY == 0 and spacesToMove == MoveL:
                    return False
                elif startY == 9 and spacesToMove == MoveR:
                    return False
                elif startY == (0 or 1) and spacesToMove == EatL:
                    return False
                elif startY == (9 or 8) and spacesToMove == EatR:
                    return False
                
                match spacesToMove:
                    case (9 | -9 | 11 | -11):
                        if board[endX][endY] == None:
                            return True
                        else :
                            return False
                    case (18 | -18 | 22 | -22):
                        middleX,middleY = int(str(int(startPos) + spacesToMove/2)[0]),int(str(int(startPos) + spacesToMove/2)[1])
                        if board[middleX][middleY][0] != turnPlayer:
                            return True
                        else:
                            return False
            elif board[startX][startY][1] :
                if turnPlayer ==0 :
                    BackR,BackL,BackEatR,BackEatL = self.associationPlayer(1)
                else:
                    BackR,BackL,BackEatR,BackEatL = self.associationPlayer(0)

                if startY == 0 and spacesToMove == BackL:
                    return False
                elif startY == 9 and spacesToMove == BackR:
                    return False
                elif startY == (0 or 1) and spacesToMove == BackEatL:
                    return False
                elif startY == (9 or 8) and spacesToMove == BackEatR:
                    return False
                
                match spacesToMove:
                    case (9 | -9 | 11 | -11):
                        if board[endX][endY] == None:
                            return True
                        else :
                            return False
                    case (18 | -18 | 22 | -22):
                        middleX,middleY = int(str(int(startPos) + spacesToMove/2)[0]),int(str(int(startPos) + spacesToMove/2)[1])
                        if board[middleX][middleY][0] != turnPlayer:
                            return True
                        else:
                            return False
            else :
                return False
        else :
            return False

    def moveToPos(self,board,startPos,endPos,turnPlayer) :
        MoveR,MoveL,EatR,EatL = self.associationPlayer(turnPlayer)
        startX,startY = int(startPos[0]),int(startPos[1])
        endX,endY = int(endPos[0]),int(endPos[1])
        if self.checkMove(board,startPos,endPos,turnPlayer):
            if int(endPos) == int(startPos) + EatL :
                middlePos = int(startPos) + MoveL
                middleX,middleY = int(str(middlePos)[0]),int(str(middlePos)[1])
                board[endX][endY] = board[startX][startY]
                board[middleX][middleY] = None
                board[startX][startY] = None
            
            elif int(endPos) == int(startPos) + EatR:
                middlePos = int(startPos) + MoveR
                middleX,middleY = int(str(middlePos)[0]),int(str(middlePos)[1])
                board[endX][endY] = board[startX][startY]
                board[middleX][middleY] = None
                board[startX][startY] = None
            elif board[startX][startY][1] == True and int(endPos) == int(startPos) - EatR:
                middlePos = int(startPos) - MoveR
                middleX,middleY = int(str(middlePos)[0]),int(str(middlePos)[1])
                board[endX][endY] = board[startX][startY]
                board[middleX][middleY] = None
                board[startX][startY] = None
            elif board[startX][startY][1] == True and int(endPos) == int(startPos) - EatL:
                middlePos = int(startPos) - MoveL
                middleX,middleY = int(str(middlePos)[0]),int(str(middlePos)[1])
                board[endX][endY] = board[startX][startY]
                board[middleX][middleY] = None
                board[startX][startY] = None
            else:
                board[endX][endY] = board[startX][startY]
                board[startX][startY] = None
            
            if (endX == 9 and turnPlayer == 1) or (endX == 0 and turnPlayer ==0):
                self.checkPromote(endX,endY,board)
            return True
        else :
            return False

    def checkPromote(self,x,y,board):
        board[x][y] = (board[x][y][0],True)
        