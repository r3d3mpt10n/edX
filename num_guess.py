x = int(input("Enter a number between 1 and 100: "))

high = 100
low = 0

guess = 0
high_low = "n"

while high_low != "c":
    guess = int((low + high) / 2)
    print("Is your number %d" % guess)
    high_low = str(input(
        "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))

    if 0 <= x < 100:

        if high_low == "h":
            high = guess

        elif high_low == "l":
            low = guess

        elif high_low == "c":
            print("Totts nailed it!")

        elif print("You totts entered something you shoudn't have"):
            break

    else:
        print("That's not between 1 and 100. I'm disappointed to say the least.")
        exit()
