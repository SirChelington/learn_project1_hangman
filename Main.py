### Das Quiz das die Welt verändert! ###
import re

# Variablen
guessed_letter = ""
result = ""

###funktionen.

# user input
def program_start(the_word, guessed_letter, result):
    guessed_letter = str(input("Eingabe: ")).upper()
    return letter_check(guessed_letter)


# Check auf länge und Buchstaben
def letter_check(guessed_letter):
    if len(guessed_letter) == 1 and re.search(r"[a-zA-Z]+", guessed_letter):
        return letter_search(guessed_letter, the_word)
    else:
        print("Bitte geben Sie nur einen Buchstaben ein.")


# suche nach passenden buchstaben.
def letter_search(guessed_letter, the_word):
    if re.search(guessed_letter, the_word):
        # gucken an welcher Stelle der Buchstabe steht.
        letter_position = []
        for index in enumerate(the_word):
            if index[1] == guessed_letter:
                letter_position.append(index[0])
        return user_Preview(guessed_letter, letter_position)
    else:
        print("Leider Falsch")


# Gelöste Buchstaben an die richtige Stelle schreiben.
def user_Preview(guessed_letter, letter_position):
    for w in range(len(letter_position)):
        place_holder[letter_position[w]] = guessed_letter
        preview = "".join(place_holder)
    print(preview.upper())
    result = preview
    return result


# User1 gibt als input das zu erratene Wort ein.
print("Guten Tag, bitte geben Sie das zu erratene Wort ohne Umlaute ein.")
the_word = str(input("Lösungswort: ")).upper()
for char in the_word:
    if re.search(r"[a-zA-Z]+", char) == None:
        print("Bitte nur Vokale und Konsonanten verwenden. Keine Umlaute.")
        exit()

place_holder = ["_"] * len(the_word)

# User2 beginnt Buchstaben zu raten.
print(
    f"Guten Tag, das gesuchte Wort hat {len(the_word)} Buchstaben. Viel Spaß beim raten."
)
print("_" * len(the_word))
while result != the_word:
    result = program_start(the_word, guessed_letter, result)
else:
    print("Gut gemacht!")
