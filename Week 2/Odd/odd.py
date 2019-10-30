def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Checks whether the number is odd or even
    while x % 2 != 0:
        return True
    return False
