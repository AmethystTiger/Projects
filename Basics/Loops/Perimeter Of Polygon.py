perimeter = 0

fx = int(input("Enter the x value: "))
fy = int(input("Enter the y value: "))

prex = fx
prey = fy

coords = input("Enter the x value (blank to quit): ")
while coords != "":
    currx = int(coords)
    curry = int(input("Enter the y value: "))

    distance = ((prex-currx)**2 + (prey-curry)**2)**0.5
    perimeter += distance

    prex = currx
    prey = curry

    coords = input("Enter the x value (blank to quit): ")

distance = ((fx-currx)**2 + (fy-curry)**2)**0.5
perimeter += distance

print(distance)
    
