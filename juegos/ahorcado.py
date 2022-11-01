# hangman.py
#importing the time module
import time
import random

turns = 10

print ("Tienes " + str(turns) + " turnos!")

print ("")

# delay
time.sleep(0.5)

# set of words to guess from
wordList = ["serapio", "musica", "python", "mitchell"]
word = random.choice(wordList)

guesses = ''

# loop till no turns are remaining
while turns > 0:
    wrong = 0

    for char in word:
        if char in guesses:
            print(char),
        else:
            print ("_"),
            wrong += 1

    print("\n")

    if wrong == 0:
        print ("Ganaste rey")
        break

    print()

    guess = ''
    if len(guess) < 1:
        while(True):
            guess = input("Ingresa una letra: ")

            if(guess != ''):
                guess = guess[0]
                break

    guesses += guess

    if guess not in word:
        turns -= 1

        print ("Equivocado")

        print ("Te quedan", + turns)

        if turns == 0:
            print ("Perdiste :(")

