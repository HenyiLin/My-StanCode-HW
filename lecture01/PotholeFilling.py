"""
File: PotholeFilling.py
Name: HenryLin
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()


def go_in():
    move()
    turn_right()
    move()


def go_out():
    turn_left()
    turn_left()
    move()
    turn_right()
    move()


    """
    pre-condition: Karel在坑的左上方，面東
    post-condition: Karel在坑的右上方，面東
    HenryLin
    """


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
