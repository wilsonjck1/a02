"""
Tests:

    >>> f(6)
    6
    >>> f(5)
    5 

"""

# This code tests your solution. Don't edit it.
import doctest
def run_tests():
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)


def f(n):
    print(n)
