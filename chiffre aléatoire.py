
import random

nombre_secret = random.randint(1, 50)

while True:
    guess = int(input("Devine le nombre entre 1 et 50 : "))

    if guess < nombre_secret:
        print("Trop petit")
    elif guess > nombre_secret:
        print("Trop grand")
    else:
        print("Bravo !")
        break