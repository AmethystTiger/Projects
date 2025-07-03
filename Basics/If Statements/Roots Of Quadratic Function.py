
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

discriminant = (b**2) - (4 * a * c)
root1 = (-b + (discriminant**0.5)) / 2 * a
root2 = (-b - (discriminant**0.5)) / 2 * a
root2 = round(root2, 2)
root1 = round(root1, 2)

if discriminant == 0:
    print("This expression has 1 real root, i.e. " + str(root1))
elif discriminant > 0:
    print("This expression has 2 real roots, i.e. " + str(root1) + " and " + str(root2))
elif discriminant < 0:
    print("This expression has no real root.")
