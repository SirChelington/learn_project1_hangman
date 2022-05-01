### Das Quiz das die Welt verändert! ###
import re

# Variablen
the_word = "Kerze".upper()
guessed_letter = ""
place_holder = ["_", "_", "_", "_", "_"]
result = ""
###funktionen.

# user input
def program_start(the_word, guessed_letter, result):
    if result != the_word:
        guessed_letter = str(input()).upper()
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


# Ausführung
while result != the_word:
    result = program_start(the_word, guessed_letter, result)
else:
    print("Gut gemacht!")
