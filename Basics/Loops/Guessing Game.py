import random

num = random.randint(1, 20)
guess_input = 0
guesses = 5

try:
    while guesses > 0:
        print(str(guesses) + " guesses left.")
        guess_input = int(input("Enter a new number between 1 and 20: "))
        guesses -= 1
        if guess_input > num:
            print("Number is too large.")
        elif guess_input < num:
            print("Number is too small.")
        elif guess_input == num:
            print("You guessed the correct number. Congratulations!!!")
            quit()
    else:
        print("Uh Oh Stinky")
        quit()
except ValueError:
    print("You didn't enter a number.\nSo sadVery bad")