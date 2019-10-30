from math import tan,pi

def polysum(n, s):
    area = (0.25*n*(s**2))/tan(pi/n)
    perimeter = n * s
    sum = area + (perimeter**2)
    return(round(sum, 4))
