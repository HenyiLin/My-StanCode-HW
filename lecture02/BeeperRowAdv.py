"""
File: BeeperRowAdv.py
Name:HenryLin
------------------------------
This program makes Karel fill up
Street 1 with some beepers already
existed
(This should be world insensitive)
"""

from karel.stanfordkarel import *
from MoveToTheEnd import *


def main():
    """
    Karel will fill the first Street in any world
    """

    while front_is_clear():
        while front_is_clear():
            if on_beeper():
                move()
            else:
                put_beeper()
                move()
        turn_around()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)