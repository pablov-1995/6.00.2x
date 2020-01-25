def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    i = 0
    while True:
        if test(i) == True:
            k = i
            break
        elif test(-i) == True:
            k = -i
            break
        i+=1
    return k