"""
File: MoveToTheEnd.py
Name:HenryLin
------------------------
This file shows how to use while loop
to walk to the end of a certain row in
karel world
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will move to the end of the first Street in any world
    """
    while front_is_clear():
        if front_is_clear():
            move()
            if on_beeper():
                pick_beeper()
        else:
            put_beeper()
            while front_is_clear():
                move()
                put_beeper()
            turn_around()




def turn_around():
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
