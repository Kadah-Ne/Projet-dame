from pion import dame
class actions:
    def __init__(self) -> None:
        self.Playable = True
        pass
    def movement(self,board,startPos,endPos,currPlayer): 
        startX,startY = self.posTranslator(board,startPos)
        endX,endY = self.posTranslator(board,endPos)
        if board[startX][startY] != " ":
            player = board[startX][startY].player
            if player != currPlayer :
                self.IllegalMove(currPlayer)
            else :
                if currPlayer == 0 and endPos - startPos > 0 and not board[startX][startY].isDame:
                    self.IllegalMove(currPlayer)
                elif currPlayer == 1 and endPos - startPos < 0 and not board[startX][startY].isDame:
                    self.IllegalMove(currPlayer)
                else:
                    if startPos+22 == endPos or startPos+18 == endPos or startPos-22 == endPos or startPos-18 == endPos: 
                        if self.checkEat(board,startPos,endPos,player):
                            if board[startX][startY] != " ":
                                board[endX][endY] = board[startX][startY]
                                board[startX][startY] = " "
                            else:
                                self.IllegalMove(player)
                        else:
                                self.IllegalMove(player)
                    elif startPos+11 == endPos or startPos+9 == endPos or startPos-11 == endPos or startPos-9 == endPos:
                        if board[startX][startY] != " ":
                                board[endX][endY] = board[startX][startY]
                                board[startX][startY] = " "
                        else:
                            self.IllegalMove(player)
                    else:
                        self.IllegalMove(player)
                    if currPlayer == 0 and endX == 0:
                        self.checkPromote(endX,endY,board)
                    elif currPlayer == 1 and endX == 9:
                        self.checkPromote(endX,endY,board)
        else:
            self.checkPromote(endX,endY,board)

    def checkEat(self,board,start,end,player):
        cheater = False
        if start+22 == end or start+18 == end or start-22 == end or start-18 == end:
            if end - start > 0 :
                if start+22 == end:
                    x,y = self.posTranslator(board,start + 11)
                    if board[x][y] != " " and board[x][y].player != player:
                        board[x][y] = " "
                    else: 
                        cheater = True
                elif start+18 == end:
                    x,y = self.posTranslator(board,start + 9)
                    if board[x][y] != " " and board[x][y].player != player :
                        board[x][y] = " "
                    else:
                        cheater = True
            elif end - start < 0:
                if start-22 == end:
                    x,y = self.posTranslator(board,start - 11)
                    if board[x][y] != " " and board[x][y].player != player :
                        board[x][y] = " "
                    else: 
                        cheater = True
                elif start-18 == end:
                    x,y = self.posTranslator(board,start - 9)
                    if board[x][y] != " " and board[x][y].player != player :
                        board[x][y] = " "
                    else:
                        cheater = True
        if not cheater :
            return(True)
        else : 
            return(False)

    def checkPromote(self,x,y,board):
        #board[x][y] = dame(board[x][y].player)
        a=1


    def posTranslator(self,board,n : int):
        cpt = n
        nbi=0
        nbj=0
        for i in board:
                cpt -= 10
                if cpt < 10:
                    for j in i:
                        
                        if cpt == 0 :
                            return(nbi,nbj)
                        cpt -= 1
                        nbj+=1
                nbi+=1

    def IllegalMove(self,player):
        print(f"Action interdite de la part du joueur {player}, fin de la partie.")
        self.Playable = False
