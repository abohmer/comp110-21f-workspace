"""This program practiced relational operators."""

__author__ = "730168318"

left_hand_side = input("Left-hand side: ")
right_hand_side = input("Right-hand side: ")

less_than = int(left_hand_side) < int(right_hand_side)
print(left_hand_side + " < " + right_hand_side + " is " + str(less_than))

greater_orequal = int(left_hand_side) >= int(right_hand_side)
print(left_hand_side + " >= " + right_hand_side + " is " + str(greater_orequal))

equal_to = int(left_hand_side) == int(right_hand_side)
print(left_hand_side + " == " + right_hand_side + " is " + str(equal_to))

not_equalto = int(left_hand_side) != int(right_hand_side)
print(left_hand_side + " != " + right_hand_side + " is " + str(not_equalto)) 