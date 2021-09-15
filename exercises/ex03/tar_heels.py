"""An exercise in remainders and boolean logic."""

__author__ = "730168318"

int_type: int = int(input("Enter an int: "))

two_remainder: int = int_type % 2

seven_remainder: int = int_type % 7 

two_seven: int = two_remainder + seven_remainder

if two_seven == 0:
    print("TAR HEELS")
else: 
    if two_remainder == 0:
        print("TAR")
    else:
        if seven_remainder == 0:
            print("HEELS")
        else: 
            print("CAROLINA")
    