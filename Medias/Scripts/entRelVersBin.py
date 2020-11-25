# Conversion entier relatif vers binaire signé
# On utilise des string pour profiter de la concaténation
n = int(input("Taille du mot : "))
entree = int(input("Entrer un entier relatif : "))
if (entree > 2 ** (n - 1) - 1) or (entree < -2 ** (n - 1)):  # Il faut que ça rentre!
    print("représentation impossible!")
else:
    sortie = str()
    if entree < 0:    # On préfère traiter les naturels
        entree += 2 ** n
    for i in range(n):
        bit = str(entree % 2)
        sortie = bit + sortie
        entree = entree // 2
    print(sortie)
