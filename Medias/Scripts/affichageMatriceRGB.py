from tkinter import * 

def represente(matrice):
    """ Représente une image à partir d'une matrice de pixels
    matrice[i][j] est le pixel situé à la colonne i et à la ligne j
    Chaque pixel est représenté par une liste de 3 couleurs RGB
    On suppose ici que chaque couleur possède 256 nuances"""
    # On extrait les informations de la matrice
    largeur = len(matrice)
    hauteur = len(matrice[0])
    # On créé une fenetre adaptée
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
