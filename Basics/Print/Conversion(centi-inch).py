centi = int(input("Write your height(in centimeters): "))

tot_inch = centi//2.54
feet = tot_inch//12
inch = tot_inch % 12

print("You are " + str(feet) + " foot, " + str(inch) + " inches.")
