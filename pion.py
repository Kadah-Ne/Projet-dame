class pion():
    def __init__(self,player):
        self.player = player
        self.isDame = False
        self.icon = None
        self.setIcon()
    
    def setIcon(self):
        if self.player == 0:
            self.icon = "x"
        else:
            self.icon = "o"
    def Movement():
        a=1

    def __str__(self) -> str:
        return self.icon

class dame(pion):
    def __init__(self,player):
        self.isDame= True
        super().__init__(player)
        

    def setIcon(self):
        if self.player == 0:
            self.icon = "χ"
        else:
            self.icon = "ϕ"

    def Movement(self):
        a=2
