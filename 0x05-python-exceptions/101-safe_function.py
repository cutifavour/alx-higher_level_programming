#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """this executes a function safely.

    Args:
        fct: is the function to execute.
        args: is the arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - send the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)

