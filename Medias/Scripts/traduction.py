EtoF = {"bread":"pain", "wine":"vin", "with":"avec", "I":"Je", "eat":"mange", "drink":"bois", "John":"Jean", "friends":"amis", "and": "et", "of":"du","red":"rouge"}
FversA = {"pain":"bread", "vin":"wine", "avec":"with", "Je":"I", "mange":"eat", "bois":"drink", "Jean":"John", "amis":"friends", "et":"and", "du":"of", "rouge":"red"}
dicts = {"English to French":EtoF, "Français vers Anglais":FversA}

def traductionMot(mot, dictionnaire):
    if mot in dictionnaire.keys():
        return dictionnaire[mot]
    elif mot != "":
        return '"' + mot + '"'
    return mot

def traduction(phrase, dicts, direction):
    majLettres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minLettres = "abcdefghijklmnopqrstuvwxyz"
    lettres = majLettres + minLettres
    dictionnaire = dicts[direction]
    traduction = ""
    mot = ""
    for c in phrase:
        if c in lettres:
            mot = mot + c
        else:
            traduction += traductionMot(mot, dictionnaire) + c
            mot = ""
    return traduction + " " + traductionMot(mot, dictionnaire)

print(traduction("I drink good red wine, and eat bread.", dicts, "English to French"))
print(traduction("Je bois du vin rouge.", dicts, "Français vers Anglais"))