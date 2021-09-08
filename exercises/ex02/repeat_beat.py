"""Repeating a beat in a loop."""

__author__ = "730168318"


beat_type: str = input("What beat do you want to repeat? ")

times_input: int = int(input("How many times do you want to repeat it? "))

beat_space = (str(" ") + beat_type)

repeat_type = beat_type

counter: int = 0
if times_input <= 0: 
    print("No beat... ")
else:
    while counter < (times_input - 1): 
        repeat_type = repeat_type + beat_space
        counter = counter + 1
    print(repeat_type)
