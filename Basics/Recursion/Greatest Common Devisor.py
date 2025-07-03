def greatest_c_d(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return greatest_c_d(b, c)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(greatest_c_d(num1, num2))