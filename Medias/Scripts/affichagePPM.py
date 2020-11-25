from tkinter import * 

source = open("Joconde.ppm","r")
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

k = 4
for j in range(hauteur):
    for i in range(largeur):
        red = int(image[k])
        redNumber = format(red, "02x")
        green = int(image[k + 1])
        greenNumber = format(green, "02x")
        blue = int(image[k + 2])
        blueNumber = format(blue, "02x")
        color = '#' + redNumber + greenNumber + blueNumber
        zoneImage.create_line(i, j, i+1, j, fill = color)
        k += 3

boutonSortir = Button(fenetre, text="Sortir", command = fenetre.destroy)
boutonSortir.pack()

fenetre.mainloop()