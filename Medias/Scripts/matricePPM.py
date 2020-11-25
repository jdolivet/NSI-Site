def matricePPM(nomFichier):
    """Entr�e : fichier image au format PPM
    Retourne une matrice de pixel
    matrice[i][j] est le pixel situ� � la colonne i et � la ligne j
    Chaque pixel est repr�sent� par une liste de 3 couleurs RGB"""
    # On transfert les donn�es du fichier dans une liste
    source = open(nomFichier,"r")
    image = source.readlines()
    source.close()
    # On pr�l�ve les informations n�cessaires
    dimensions = image[2].split()
    largeur = int(dimensions[0])
    print("Largeur de l'image :", largeur)
    hauteur = int(dimensions[1])
    print("Hauteur de l'image :", hauteur)
    nuances = image[3]
    print("Nuances de couleurs :", nuances)
    # On construit la matrice
    octet = 4
    matrice = [[0 for j in range(hauteur)] for i in range(largeur)]
    for j in range(hauteur):
        for i in range(largeur):
            pixel=[0,0,0]
            for k in range(3):
                pixel[k] = int(image[octet])
                octet += 1
            matrice[i][j] = pixel
    return matrice