longest = ''
current = ''
# Iterate over the given string
for i in range(len(s)):
    # ord is used for getting ASCII value of the character
    # Check whether the next alphabet is greater than the present alphabet and update the current string
    if ord(s[i]) >= ord(s[i-1]):
        current += s[i]
    # If the next alphabet is smaller then the present alphabet reset the current string from present character
    else:
        current = s[i]
    # Updating the longest string
    if len(current) > len(longest):
        longest = current
print(longest)
