from tkinter import * 

source = open("Joconde.pbm","r")
image = source.readlines()
source.close()

commentaire = image[1][1:]
dimensions = image[2].split()
largeur = int(dimensions[0])
hauteur = int(dimensions[1])

fenetre = Tk()
fenetre.title("Lecture d'une image")
label = Label(fenetre, text = commentaire)
label.pack()
zoneImage = Canvas(fenetre, width = largeur, height = hauteur)
zoneImage.pack()


for j in range(hauteur):
    for i in range(largeur):
        if image[j + 3][i] == '1':
            zoneImage.create_line(i, j, i+1, j, fill = "BLACK")
        else:
            zoneImage.create_line(i, j, i+1, j, fill = "WHITE")

boutonSortir = Button(fenetre, text="Sortir", command = fenetre.destroy)
boutonSortir.pack()

fenetre.mainloop()
