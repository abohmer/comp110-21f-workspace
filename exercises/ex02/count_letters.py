"""Counting letters in a string."""

__author__ = "730168318"

letter_type: str = input("What letter do you wanna search for?: ")

enter_word: str = input("Enter a word: ")

i: int = 0

count = 0

while i < (len(enter_word) - 1):
    if enter_word[i] == letter_type:
        count = count + 1
    i = i + 1
print("Count: " + str(count))
