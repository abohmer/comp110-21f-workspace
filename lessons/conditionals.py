"""An example of conditional (if-else) statements"""

SECRET: int = 3

# all capital name is one that is a constant, we don't 
# plan on changing it later on in our program 

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET: 
    print("You guessed correctly!!!!")
    print("Have a wonderful day!!!")
else: 
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else: 
        print("You quessed too low!")
        
print("Game over.")
