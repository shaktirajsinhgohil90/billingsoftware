secret = 7

while True:
    guess = int(input("guess the number (1-10): "))

    if guess == secret:
        print("you win!")
        break
    else:
        print("* try again")

