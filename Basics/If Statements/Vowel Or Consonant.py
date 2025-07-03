
letter = str(input("Enter a letter: "))

if len(letter) > 1:
    print("Please enter a single letter.")
    quit()
elif letter == "y":
    print("Sometimes y is a vowel and sometimes y is a consonant.")
elif letter != "a" and "e" and "i" and "o" and "u" and "y":
    print(letter + " is a consonant.")
elif letter == "a" or "e" or "i" or "o" or "u":
    print(letter + " is a vowel.")
