"""Finding duplicate letters in a word."""

__author__ = "730168318"

duplicate_word: str = input("Enter a word: ")

duplicate_index = []

for char in duplicate_word:
    if duplicate_word.count(char) > 1:
        if char not in duplicate_index:
            duplicate_index.append(char)

duplicate_counter = len(duplicate_index)

if duplicate_counter >= 1: 
    print("True")
else: 
    print("False")
