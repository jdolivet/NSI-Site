# Conversion binaire signé de 64 bits vers flottant (uniquement normalisé)
# On utilise des string pour profiter du slicing
entree = input("Entrer un nombre binaire de taille 64 : ")
signe = entree[0]
expBin = entree[1:12]
mantisseBin = entree[12:64]
# L'exposant
exposant = int(expBin, 2) - 1023
# La mantisse
mantisse = 1.0
for i in range(52):
    mantisse += int(mantisseBin[i]) / (2 ** (i + 1))
# Le nombre signé
if signe == '1':
    mantisse *= -1
sortie = mantisse * (2 ** exposant)
print("Le nombre représenté est : ", mantisse, "* 2^(", exposant, ")") 
print("Le flottant est : ", sortie)
