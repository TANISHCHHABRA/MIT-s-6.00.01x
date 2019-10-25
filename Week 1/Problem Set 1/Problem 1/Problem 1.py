vowels=['a','e','i','o','u']
count = 0
# Iterate over every charcter in given string
for letter in s:
    # If character is a vowel
    if letter in vowels:
        count += 1
print(count)
