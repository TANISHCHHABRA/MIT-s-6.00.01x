count = 0
# Iterate over the length of given string 
for i in range(len(s)):
    # If bob occurs
    if s[i:i+3] == "bob":
        count += 1
print(count)
