longest = ''
current = ''
for i in range(len(s)):
    if ord(s[i]) >= ord(s[i-1]):
        current += s[i]
    else:
        current = s[i]
    if len(current) > len(longest):
        longest = current
print(longest)
