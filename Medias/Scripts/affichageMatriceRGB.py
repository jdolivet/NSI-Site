from tkinter import * 

def represente(matrice):
    """ Repr�sente une image � partir d'une matrice de pixels
    matrice[i][j] est le pixel situ� � la colonne i et � la ligne j
    Chaque pixel est repr�sent� par une liste de 3 couleurs RGB
    On suppose ici que chaque couleur poss�de 256 nuances"""
    # On extrait les informations de la matrice
    largeur = len(matrice)
    hauteur = len(matrice[0])
    # On cr�� une fenetre adapt�e
    fenetre = Tk()
    fenetre.title("Lecture d'une image")
    zoneImage = Canvas(fenetre, width = largeur, height = hauteur)
    zoneImage.pack()
    # On trace les pixels
    for j in range(hauteur):
        for i in range(largeur):
            red = matrice[i][j][0]
            redNumber = format(red, "02x")
            green = matrice[i][j][1]
            greenNumber = format(green, "02x")
            blue = matrice[i][j][2]
            blueNumber = format(blue, "02x")
            color = '#' + redNumber + greenNumber + blueNumber
            zoneImage.create_line(i, j, i + 1, j, fill = color)
    # On ajoute un bouton pour sortir
    boutonSortir = Button(fenetre, text="Sortir", command = fenetre.destroy)
    boutonSortir.pack()
    # On commande l'affichage
    fenetre.mainloop()
