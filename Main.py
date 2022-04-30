### Das Quiz das die Welt verändert! ### 
import re

#Variablen
dasWort = str("Kerze").upper()
gw = str("")
hangman = ["_","_","_","_","_"]
gelöst = ""
###funktionen.

#user input
def programm_start(dasWort, gw, gelöst):
    if gelöst != dasWort:
        gw = str(input()).upper()
        gelöst = lettercheck(gw)
        return gelöst

#Check auf länge und Buchstaben             
def lettercheck(gw):
    if len(gw) == 1 and re.search(r"[a-zA-Z]+",gw):
        gelöst = buchstabenSuche(gw, dasWort)
        return gelöst
    else:
        print("Bitte geben Sie nur einen Buchstaben ein.")

#suche nach passenden buchstaben.
def buchstabenSuche(gw, dasWort):
    if re.search(gw, dasWort):
        #gucken an welcher Stelle der Buchstabe steht.
        bPosition = [i for i, x in enumerate(dasWort) if x == gw]
        gelöst = user_Preview(gw, bPosition)
        return gelöst
    else: 
        print("Leider Falsch")

#Gelöste Buchstaben an die richtige Stelle schreiben.
def user_Preview(gw, bPosition):
    for w in range(len(bPosition)):
        hangman[bPosition[w]] = gw
        preview = "".join(hangman)
    print(preview.upper())
    gelöst = preview
    return gelöst
        


#Ausführung
while gelöst != dasWort:
    gelöst = programm_start(dasWort, gw, gelöst)
else:
    print("Gut gemacht!")
