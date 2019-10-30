def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x = a
    while True:
        # Checks whether x is divisble by both a and b
        if (a % x == 0) & (b % x == 0):
            return x
            break
        # Updating x
        x -= 1
