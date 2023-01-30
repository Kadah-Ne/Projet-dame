
class damier :
    def __init__(self):
        self.Board = []
        self.IABoard = []
        self.BlackPawn = (1,False) #pion(1)
        self.WhitePawn = (0,False) #pion(0)
        self.WhiteQueen = (0,True) #dame(0)
        self.BlackQueen = (1,True) #dame(1)
        self.createBoard()
        self.convertIA()

        
    def createBoard(self):
        for i in range(0,10):
            self.Board.append([])
        self.populateBoard()
    
    def populateBoard(self):
        cpt = 0
        for i in self.Board:
            if cpt != 4 or cpt!=5:
                if 0<=cpt<=3  and cpt%2 == 0:
                    cptPawn = 0
                    for j in range (0,10):
                        if j%2 != 0 :
                            i.append(self.BlackPawn)
                            cptPawn+=1
                            if cptPawn == 5:
                                break
                        else :
                            i.append(None)
                elif 0<=cpt<=3  and cpt%2 != 0: 
                    cptPawn = 0
                    for j in range (0,10):
                        if j%2 == 0 :
                            i.append(self.BlackPawn)
                            cptPawn+=1
                            if cptPawn == 5:
                                i.append(None)
                                break
                        else :
                            i.append(None)
                elif 6<=cpt<=9  and cpt%2 == 0: 
                    cptPawn = 0
                    for j in range (0,10):
                        if j%2 != 0 :
                            i.append(self.WhitePawn)
                            cptPawn+=1
                            if cptPawn == 5:
                                break
                        else :
                            i.append(None)
                elif 6<=cpt<=9  and cpt%2 != 0: 
                    cptPawn = 0
                    for j in range (0,10):
                        if j%2 == 0 :
                            i.append(self.WhitePawn)
                            cptPawn+=1
                            if cptPawn == 5:
                                i.append(None)
                                break
                        else :
                            i.append(None)
                else :
                    for j in range(0,10):
                        i.append(None)
            cpt+=1

    def convertIA(self):
        self.IABoard = []
        for i in self.Board:
            for j in i:
                if j == self.WhitePawn:
                    self.IABoard.append((0,False))
                elif j == self.BlackPawn:
                    self.IABoard.append((1,False))
                elif j == self.WhiteQueen:
                    self.IABoard.append((0,True))
                elif j == self.BlackQueen:
                    self.IABoard.append((1,True))
                else:
                    self.IABoard.append(None)
    
    def printBoard(self,testBoard = None):
        if not testBoard :
            testBoard = self.IABoard
        aze = "| |"
        for a in range(10):
            aze += "|"+str(a)+"|"
        print(aze)
        cpt = 0
        cpta = 0
        Ligne = ""        
        for i in testBoard:
            if cpt == 0 : 
                Ligne += f"|{cpta}|"
                cpta +=1
            if i == (1,False):
                Ligne += "|x|"
            elif i == (0,False):
                Ligne += "|o|"
            elif i == (1,False):
                Ligne += "|X|"
            elif i == (1,False):
                Ligne += "|O|"
            else:
                Ligne += "| |"
            cpt +=1
            if cpt >= 10:
                print(Ligne)
                Ligne = ""
                cpt = 0

    def printBoardT(self):
        aze = "| |"
        for a in range(10):
            aze += "|"+str(a)+"|"
        print(aze)
        cpt = 0
        cpta = 0
        Ligne = ""        
        for j in self.Board:
            for i in j:
                if cpt == 0 : 
                    Ligne += f"|{cpta}|"
                    cpta +=1
                if i == self.BlackPawn:
                    Ligne += "|x|"
                elif i == self.WhitePawn:
                    Ligne += "|o|"
                elif i == self.WhiteQueen:
                    Ligne += "|X|"
                elif i == self.WhitePawn:
                    Ligne += "|O|"
                else:
                    Ligne += "| |"
                cpt +=1
                if cpt >= 10:
                    print(Ligne)
                    Ligne = ""
                    cpt = 0

            

