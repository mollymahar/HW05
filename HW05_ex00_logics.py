#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    number = raw_input("Enter a number: ")
    try:
        number_int = eval(number)
    except:
        print "Not a valid number."
    else:
        if number_int % 2 == 0:
            print "even"
        else: 
            print "odd"
    return None


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for i in range(1,101):
        if i % 10 == 1:                             # creates new row after each 10
            print "\n"
        print str((4 - len(str(i))) * ' ') + str(i),



def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    print "\n"                                      # newline since this runs after the grid
    count = 0
    total = 0.0                                     # use float division
    while True:
        user_entry = raw_input("Enter your numbers: ")
        if user_entry == 'done':                    # if user is done, exit the function
            return total / count                    # calculates and returns avg as float
        else:
            try:
                user_entry = eval(user_entry)
            except:
                print "Not a number."
                return None
            else:
                total += user_entry
                count += 1


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print find_average()

if __name__ == '__main__':
    main()
