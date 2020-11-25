# Conversion flottant vers binaire 64bits
# On utilise des string pour pouvoir profiter de la concatenation
# Un nombre décimal s'ecrit avec un '.'
entree = float(input("Entrer un nombre décimal : "))
# Le signe
signe = str()
if entree < 0:    
    signeBin = '1'
    signe = '-'     # Pour l'affichage intermediaire
else:
    signeBin = '0'
entree = abs(entree)
# On transforme l'ecriture : entree = mantisse * 2 exposant
exposant = 0
if entree > 1.0:
    while 2 ** exposant <= entree:
        exposant += 1
    exposant = exposant - 1
else:
    while 2 ** exposant > entree:
        exposant -= 1
mantisse = entree / (2 ** exposant)
print("Le nombre a représenter est :", signe, mantisse, "* 2^(", exposant, ")")
# Exposant
expBin = bin(1023 + exposant)
expBin = expBin[2:]         # On se debarasse du '0b'
while len(expBin) < 11:
    expBin = '0' + expBin
# Mantisse
mantisse = mantisse - 1.0
mantisseBin = str()
for i in range(52):     
    if (2 ** -(i+1)) <= mantisse:
        mantisseBin += '1'
        mantisse -= (2 ** -(i+1))     
    else:
        mantisseBin += '0'
# On colle tout
sortie = signeBin + expBin + mantisseBin
print("La représentation machine est :", sortie)

