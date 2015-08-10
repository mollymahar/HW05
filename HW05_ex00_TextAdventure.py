#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
import sys

# Body


def infinite_stairway_room(username, count=0):
    print "%s walks through the door to see a dimly lit hallway." % username
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print '%s takes the stairs' % username
        if (count > 0):
            print "but %s is not happy about it" % username
        infinite_stairway_room(username, count + 1)
    # option 2 == ?????
    if next == option_2:
        pass


def gold_room(username):
    print "This room is full of gold.  How much does %s take?" % username

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, %s is not greedy, %s wins!" % (username, username)
        exit(0)
    else:
        dead("%s is a greedy bastard!" % username)


def bear_room(username):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is %s going to move the bear?" % username
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey" or "take" or "honey":
            dead("The bear looks at %s then slaps %s's face off." % (username, username))
        elif next == ("taunt bear" or "taunt") and not bear_moved:
            print "The bear has moved from the door. %s can go through it now." % username
            bear_moved = True
        elif next == ("taunt bear" or "taunt") and bear_moved:
            dead("The bear gets pissed off and chews %s's leg off." % username)
        elif next == ("open door" or "open" or "door") and bear_moved:
            gold_room(username)
        else:
            print "I got no idea what that means."


def cthulhu_room(username):
    print "Here %s sees the great evil Cthulhu." % username
    print "He, it, whatever stares at %s and %s goes insane." % (username, username)
    print "Does %s flee for %s's life or eat %s's head?" % (username, username, username)

    next = raw_input("> ")

    if "flee" in next:
        infinite_stairway_room(username, 0)
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(username)


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    username = sys.argv[1]
    print "%s is in a dark room." % username
    print "There is a door to %s's right and left." % username
    print "Which one does %s take?" % username

    next = raw_input("> ")

    if next == "left":
        bear_room(username)
    elif next == "right":
        cthulhu_room(username)
    else:
        dead("%s stumbles around the room until %s starves." % (username, username))

if __name__ == '__main__':
    main()
