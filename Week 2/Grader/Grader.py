# Tanish

# Import Tan and pi function from math library
from math import tan,pi

# Define a function Polysum
def polysum(n, s):
    
    # Compute the area off the polygon
    area = (0.25*n*(s**2))/tan(pi/n)
    
    # Compute perimeter of polygon
    perimeter = n * s
    
    # Compute the sum of area and square of perimeter
    sum = area + (perimeter**2)
    
    # Return the sum by rounding it to 4 decimal numbers
    return(sum)
