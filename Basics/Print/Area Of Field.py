
w = float(input("Enter the width of the land in feet: "))
l = float(input("Enter the length of the room in feet: "))

a = l * w
area = a/43560
round(area, 1)

print("The area is " + str(area) + " acres.")

