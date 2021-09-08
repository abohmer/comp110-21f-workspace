"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730168318"
from random import randint
randint_output: int = randint(1, 4)

print("Your fortune cookie says...")

if randint_output == 1:
    print("You will soon find the love of your life ")
else: 
    if randint_output == 2:
        print("You will die alone")
    else:
        if randint_output == 3:
            print("You will soon find lots of money")
        else:
            if randint_output == 4:
                print("You will find that flattery goes far tonight")

print("Now, go spread positive vibes!")
