low = 1
high = 1000
print("Think of a number between {} and {}".format(low, high))
input("press ENTER to start the game")
guess = 1
while True:
    print("running the code between {} and {}".format(low, high))
    pos = low + (high - low) // 2
    high_low = input("my guess is {}. If your guess is greater than my guess type h "
                     "and if lower than my guess type l or if i am correct type c: "
                     .format(pos)).casefold()

    if high_low == 'h':
        low = pos + 1
    elif high_low == 'l':
        high = pos - 1
    elif high_low == 'c':
        print("i got it in {} number of guesses".format(guess))
        break
    else:
        print("PLease enter h,l or c")
    guess += 1

