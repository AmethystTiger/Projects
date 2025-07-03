
year = int(input("Enter a year: "))

symbol = year % 12

if symbol == 0:
    print(str(year) + " is the year of the Monkey.")
elif symbol == 1:
    print(str(year) + " is the year of the Rooster.")
elif symbol == 2:
    print(str(year) + " is the year of the Dog.")
elif symbol == 3:
    print(str(year) + " is the year of the Pig.")
elif symbol == 4:
    print(str(year) + " is the year of the Rat.")
elif symbol == 5:
    print(str(year) + " is the year of the Ox.")
elif symbol == 6:
    print(str(year) + " is the year of the Tiger.")
elif symbol == 7:
    print(str(year) + " is the year of the Hare.")
elif symbol == 8:
    print(str(year) + " is the year of the Dragon.")
elif symbol == 9:
    print(str(year) + " is the year of the Snake.")
elif symbol == 10:
    print(str(year) + " is the year of the Horse.")
elif symbol == 11:
    print(str(year) + " is the year of the Sheep.")

