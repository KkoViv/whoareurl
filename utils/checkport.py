#!/usr/bin/python3

# File Description : This file supports the port validation for argparse

# General pipeline:
# - convert the str argument in int
# - check if the argument is in the tCP port range
# - return a int or raise an error

###################################
# IMPORTED MODULES
###################################

from argparse import ArgumentTypeError

###################################
# IMPORTED FUNCTIONS
###################################

# N/A

###################################
# FUNCTIONS
###################################

def checkport(port):
    
    try:
        check = int(port)
        if check in range (1,65535+1):
            return check
        else:
            raise ArgumentTypeError ("The port value must be in range 1 - 65535")
    except ValueError:
        raise ArgumentTypeError ("The port value must be an integer")
