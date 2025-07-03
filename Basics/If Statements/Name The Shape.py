
no_of_sides = int(input("Enter the number of sides of the shape: "))

if no_of_sides == 3:
    print("The shape with three sides is a Triangle.")
elif no_of_sides == 4:
    print("The shape with four sides is a Square.")
elif no_of_sides == 5:
    print("The shape with five sides is a Pentagon.")
elif no_of_sides == 6:
    print("The shape with six sides is a Hexagon.")
elif no_of_sides == 7:
    print("The shape with seven sides is a Heptagon.")
elif no_of_sides == 8:
    print("The shape with eight sides is a Octagon.")
elif no_of_sides == 9:
    print("The shape with nine sides is a Nonagon.")
elif no_of_sides == 10:
    print("The shape with ten sides is a Decagon.")
elif no_of_sides > 10 or no_of_sides < 3:
    print("Please enter a no. between 3 and 10.")
    quit()

