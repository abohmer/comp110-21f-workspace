"""Drawing forests in a loop."""

__author__ = "730168318"

TREE: str = '\U0001F332'

depth_input: int = int(input("Depth: "))

i: int = 1
if depth_input >= 1:
    while i < (depth_input + 1):
      # tree_space = TREE + tree_space
        tree_repeat = TREE * i 
        i = i + 1
        print(tree_repeat)
