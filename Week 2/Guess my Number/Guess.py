print("Please think of a number between 0 and 100!")
l = 0
h = 100

while True :
    avg = (l + h)//2
    print("Is your secret number " ,avg,"?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans =='h' :
        h = avg
    elif ans == 'l' :
        l = avg
    elif ans == 'c' :
        print("Game over. Your secret number was: " , avg)
        break
    else:
        print("Sorry, I did not understand your input.")
None
