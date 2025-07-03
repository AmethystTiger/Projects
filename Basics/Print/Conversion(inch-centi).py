feet = int(input("Write your height(in feet): "))
inch = int(input("Write your height(in inches): "))

inch = (feet * 12) + inch

centi = inch * 2.54
centi = round(centi, 2)

print("Your height in centimeters is " + str(centi))
