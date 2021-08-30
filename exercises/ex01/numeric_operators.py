"""This program practices numberic operators, type conversions, and string concatenation."""

__author__ = "730168318"


# Get input for first and second number and store in unique variables
left_hand_side = input("Left-hand side: ")
right_hand_side = input("Right-hand side: ")

# Raise left input to the power of right input variable and print
exponent_input = int(left_hand_side) ** int(right_hand_side)
print(left_hand_side + " ** " + right_hand_side + " is " + str(exponent_input)) 

# Floor divide left input by right input and print
divide_input = int(left_hand_side) / int(right_hand_side) 
print(left_hand_side + " / " + right_hand_side + " is " + str(divide_input))

integer_divsion = int(left_hand_side) // int(right_hand_side)
print(left_hand_side + " // " + right_hand_side + " is " + str(integer_divsion))

remainder_input = int(left_hand_side) % int(right_hand_side)
print(left_hand_side + " % " + right_hand_side + " is " + str(remainder_input))

