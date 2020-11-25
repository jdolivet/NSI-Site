def editeur(nomFichier, base = "hex", start = 0, end = -1, nbCol = 16, sep = True, affLigne = True):
    """
    Permet la lecture d'un fichier octet par octet
    Paramètres :
        nomFichier  : str, le nom du fichier à lire
            Le fichier doit etre dans le meme repertoire
    Options :
        start : int (default = 0)
        end   : int (default = 0)
        base  : str (default : hex)
            hex : affichage octet et n° ligne en ecriture hexa
            bin : affichage octet en binaire et n° ligne en hexa
            dec : affichage octet et n° ligne en décimal
    Forme :
        nbCol    : int, nb d'octets par ligne (default = 16)
        sep      : boolean, séparateur entre octet (default = True)
        affLigne : boolean, affiche le nb d'octet précédents (default = True)
      
    """
    
    source = open(nomFichier, "rb")
    fichier = source.read()
    source.close()
    
    longueur = len(fichier)
    print("Le fichier contient", longueur, "octets")
        
    if base == "hex":
        formRep = '02x'
        formCol = '06x'
    if base == "dec":
        formRep = '03'
        formCol = '06'
    if base == "bin":
        formRep = '08b'
        formCol = '06x'

    if end == -1:
        end = longueur
        
    if sep == True:
        formSep = ' '
    else:
        formSep = ''
        

    col = 0
    for i in range(start, end):
        octet = format(fichier[i], formRep)
        if col % nbCol == 0:
            if affLigne == True:
                print('\n', format(col, formCol), ": ", end = '')
            else:
                print()
        col += 1
        print(octet, end = formSep)           
