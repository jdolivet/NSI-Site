# Conversion binaire signé vers entier relatif
# On utilise des string pour pouvoir accéder aux positions des chiffres
n = int(input("taille du mot : "))
entree = input("Entrer un nombre binaire de taille " + str(n) + " : ")
if len(entree) != n:
    print("conversion impossible!")
total = 0
for i in range(n):
    bit = int(entree[i])
    total += bit * 2 ** (n - i - 1) 
if entree[0] == "1":  # Il s'agit alors d'un nombre négatif
    total -= 2 ** n
print(total)

