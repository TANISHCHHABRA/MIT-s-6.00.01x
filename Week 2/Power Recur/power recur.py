def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Base Case
    if exp == 0:
         return 1
    # Calling the function aain and updating the ans
    ans = base * recurPower(base, exp - 1)
    return ans
