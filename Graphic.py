import tkinter as tk

class graph :
    def __init__(self) -> None:
        self.fenetre = tk.Tk()
        self.fenetre.title("Jeu de dames")
        self.canvas = tk.Canvas(self.fenetre, width=600, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.pion_clique)
        
    async def dessinePlateau(self):
        for i in range(10):
            for j in range(10):
                couleur = "white" if (i + j) % 2 == 0 else "lightgrey"
                x1, y1 = i * 50, j * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")
    
    def dessinePions(self,board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != None and board[i][j][0] == 1:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="black")
                elif board[i][j] != None and board[i][j][0] == 0:
                    self.canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="white")

    def pion_clique(self,event):
        # Récupérer les coordonnées du clic de la souris
        x, y = event.x, event.y
        # Calculer la ligne et la colonne du pion sélectionné
        ligne = x // 50
        colonne = y // 50
        # Afficher les coordonnées du pion sélectionné
        print(f"Pion sélectionné : ligne {ligne}, colonne {colonne}")
    
    
