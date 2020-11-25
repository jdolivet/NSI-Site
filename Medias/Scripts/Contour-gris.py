from turtle import * 


def matricePGM(nomFichier):
    source = open(nomFichier,"r")
    image = source.readlines()
    source.close()

    dimensions = image[2].split()
    largeur = int(dimensions[0])
    hauteur = int(dimensions[1])
    
    octet = 4
    matrice = [[0 for j in range(hauteur)] for i in range(largeur)]
    for j in range(hauteur):
        for i in range(largeur):
            pixel = int(image[octet])
            octet += 1
            matrice[i][j] = pixel
    return matrice

def contour(bitmap, seuil):
    largeur = len(bitmap)
    hauteur = len(bitmap[0])
    for j in range(hauteur):
        for i in range(largeur):
            if abs(bitmap[max(i-1,0)][j]-bitmap[i][j])+abs(bitmap[i][min(j+1,largeur-1)]-bitmap[i][j])>seuil:
                down()
            else:
                up()
            goto(i + 1, -j)
        up()
        goto(0, -j)
        down()

matrice = matricePGM("Joconde.pgm")
contour(matrice, 25)
