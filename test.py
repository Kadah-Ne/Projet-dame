import tkinter as tk

def afficher_plateau():
    # Créer une fenêtre tkinter
    fenetre = tk.Tk()
    fenetre.title("Jeu de Dames")

    # Créer un canvas dans la fenêtre pour dessiner le plateau de jeu
    canvas = tk.Canvas(fenetre, width=600, height=600)
    canvas.pack()

    # Dessiner le plateau de jeu en dessinant des carrés blancs et noirs
    for i in range(10):
        for j in range(10):
            couleur = "white" if (i + j) % 2 == 0 else "lightgrey"
            x1, y1 = i * 50, j * 50
            x2, y2 = x1 + 50, y1 + 50
            canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")

    # Dessiner les pions sur le plateau
    canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="black")
    canvas.create_oval(j * 50 + 10, i * 50 + 10, j * 50 + 40, i * 50 + 40, fill="white")

    # Ajouter une gestion d'événement pour savoir si un joueur a cliqué sur un pion
    def pion_clique(event):
        # Récupérer les coordonnées du clic de la souris
        x, y = event.x, event.y
        # Calculer la ligne et la colonne du pion sélectionné
        ligne = x // 50
        colonne = y // 50
        # Afficher les coordonnées du pion sélectionné
        print(f"Pion sélectionné : ligne {ligne}, colonne {colonne}")

    canvas.bind("<Button-1>", pion_clique)

    # Afficher la fenêtre
    fenetre.mainloop()

# Exemple d'utilisation
afficher_plateau()
