# Conversion entier vers binaire
entree = int(input("Entrer un entier naturel : "))
sortie = str()  # On utilise des string pour pouvoir concaténer et ainsi positionner correctement les bits
while entree != 0:
    bit = str(entree % 2)
    sortie = bit + sortie   # on concatène à gauche car on commence par les bits faibles
    entree = entree // 2
print(sortie)
