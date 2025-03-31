"""
File: Steeplechase.py
Name: HenryLin
---------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """


    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    Pre-condition:karel在欄杆左邊，面東
    Post-condition:karel在欄杆右，靠牆
    """
    up()
    cross()
    down()


def up():
    turn_left()
    while not right_is_clear():
        move()


def cross():
    turn_right()
    move()
    turn_right()


def down():
    while front_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
