class Noeud:
    """ Noeud du dictionnaire """

    def __init__(self, caractere):
        """ Constructeur du noeud
        Attributs : un caractère et une liste de fils """
        self.lettre = caractere
        self.fils = []

    def __str__(self):
        """ Configuration de l'impression """
        sb = ''
        sb += self.lettre
        if (self.fils != []):
            sb += '('
            for noeuds in self.fils:
                sb += str(noeuds) + ','
            sb = sb[:-1]
            sb += ')'
        return sb
        
    def ajouteFils(self, noeud):
        """ Ajoute un fils au noeud courant """
        self.fils.append(noeud)

    def existeMotRecursif(self, mot, position):
        """ Cette methode verifie si le nœud courant a bien
        un fils contenant le caractere mot[pos].
        Dans ce cas on essaye de lire la suite
        du mot à partir de ce caractère.  """
        existe = True
        if (position < len(mot)):
            for elts in self.fils:
                if (elts.lettre == mot[position]):
                    existe = True
                    return elts.existeMotRecursif(mot, position + 1)
                else:
                    existe = False
        for elts in self.fils:           
            if (elts.lettre == '*'):
                break
            else:
                existe = False
        return existe

    def listeMotsAlphabetique(self, prefixe):
        """ Cette methode prend la liste des caracteres rencontres sur
        le chemin menant au Noeud courant, appelee prefixe  """
        if (self.lettre == '*'):
            mot = ''
            for caractere in prefixe:
                mot += caractere
            print(mot[1:])
        else:
            temp = prefixe
            temp += self.lettre
            for elts in self.fils:
                elts.listeMotsAlphabetique(temp)


class Dictionnaire:
    """ Classe dictionnaire """

    def __init__(self):
        """ Constructeur du dictionnaire
        Attribut : la racine du dictionnaire """
        self.racine = Noeud('_')

    def __str__(self):
        """ Configuration de l'impression """
        return str(self.racine)

    def existeMot(self, mot):
        """ Cette methode verifie la presence d'un mot
        dans le dictionnaire """
        return self.racine.existeMotRecursif(mot, 0)

    def estPrefixe(self, mot):
        """ Cette methode verifie si le mot est prefixe d'un mot du dictionnaire.
        Rappel : etre prefixe veut dire etre le debut d'un mot du dictionnaire."""
        noeud = self.racine
        prefixe = False
        i = 0
        while (noeud.fils != [] and i < len(mot)):
            for elts in noeud.fils:
                if elts.lettre == mot[i]:
                    prefixe = True
                    noeud = elts
                    i += 1
                    break
                else:
                    prefixe = False
            if prefixe == False:
                break
        return prefixe

    def ajouteMot(self, mot):
        """ Cette methode permet de construire le dictionnaire
        a partir des mots.
        Retourne True si le mot a bien ete ajoute et
        False si le mot etait deja present dans le dictionnaire."""
        noeud = self.racine
        deja = True
        i = 0
        while (noeud.fils != [] and i < len(mot)):
            for elts in noeud.fils: 
                if elts.lettre == mot[i]:
                    deja = False
                    noeud = elts
                    i += 1
                    break
                else:
                    deja = True
            if deja == True:
                break
        for j in range(i, len(mot)):
            ajout = Noeud(mot[j])
            k = 0
            for elts in noeud.fils:
                if (elts.lettre > ajout.lettre):
                    k += 1
            noeud.fils.insert(len(noeud.fils) - k, ajout)
            noeud = ajout
        if deja == False:
            for elts in noeud.fils:
                if elts.lettre == '*':
                    break
                else:
                    deja = True
        if deja == True:
            fin = Noeud('*')
            noeud.fils.insert(0, fin)
        return deja

    def listeMotsAlphabetique(self):
        """ Cette methode affiche les mots contenus
        dans le dictionnaire et ce par ordre alphabétique """
        self.racine.listeMotsAlphabetique('')

# Tests existence
print("Tests existence : ")
a1 = Noeud('*')
a2 = Noeud('*')
a3 = Noeud('*')
b = Noeud('l')
c = Noeud('e')
d = Noeud('a')
e = Noeud('s')
b.ajouteFils(c)
b.ajouteFils(d)
c.ajouteFils(e)
c.ajouteFils(a1)
d.ajouteFils(a2)
e.ajouteFils(a3)
print(b)
dico = Dictionnaire()
dico.racine.ajouteFils(b)
print(dico)
print(dico.existeMot(""))
print(dico.existeMot("la"))
print(dico.existeMot("les"))
print(dico.existeMot("sa"))
print(dico.existeMot("se"))
print(dico.existeMot("lu"))
print(dico.existeMot("l"))
print('')

#Tests ajout
print("Tests ajout : ")
dico = Dictionnaire()
print(dico)
b1 = dico.ajouteMot("le")
print(dico)
b2 = dico.ajouteMot("loup")
print(dico)
dico.ajouteMot("les")
print(dico)
dico.ajouteMot("louve")
print(dico)
print(dico.existeMot("le"))
print(dico.existeMot("les"))
print(dico.existeMot("lou"))
print(dico.existeMot("lesa"))
print(dico.existeMot("loupp"))
print(dico.ajouteMot("le"))
print(dico.ajouteMot("loup"))
print(dico.ajouteMot("louv"))
print(dico.ajouteMot("lulu"))
print(b1)
print(b2)
print('')

# Tests prefixe
print("Tests prefixe : ")
dico = Dictionnaire()
dico.ajouteMot("le")
dico.ajouteMot("loup")
dico.ajouteMot("les")
dico.ajouteMot("louve")
print(dico.estPrefixe("le"))
print(dico.estPrefixe("les"))
print(dico.estPrefixe("lou"))
print(dico.estPrefixe("lu"))
print('')

# Tests enumeration
print("Tests enumeration : ")
dico =  Dictionnaire()
dico.ajouteMot("an")
dico.ajouteMot("an")
dico.ajouteMot("le")
dico.ajouteMot("gaz")
dico.ajouteMot("louv")
dico.ajouteMot("loup")
dico.ajouteMot("les")
dico.ajouteMot("louve")
dico.listeMotsAlphabetique()
print('')

# Importation du dictionnaire de la langue française sans accents
print("Importation du dictionnaire de la langue française sans accents")
# On cree la variable dico qui est une instance de la classe Dictionnaire
dico = Dictionnaire()
# on recupere les mots dans un fichier texte
fichier = open("dico.txt", 'r')
for ligne in fichier:
  # on ajoute chaque mot au dictionnaire
  dico.ajouteMot(ligne[:-1])
fichier.close()
print("Done!")
print("Le dictionnaire est dans la variable dico!")

