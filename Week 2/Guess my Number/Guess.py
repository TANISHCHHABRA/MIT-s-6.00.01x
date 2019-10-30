print("Please think of a number between 0 and 100!")
l = 0
h = 100

while True :
    # Changes the avg value
    avg = (l + h)//2
    # Ask the user whether the guess is high, low or correct
    print("Is your secret number " ,avg,"?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    # If the guess is high
    if ans =='h' :
        h = avg
    # If the guess is low
    elif ans == 'l' :
        l = avg
    # If the guess is correct
    elif ans == 'c' :
        print("Game over. Your secret number was: " , avg)
        break
    else:
        print("Sorry, I did not understand your input.")
None
