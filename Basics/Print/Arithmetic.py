from math import log10

a = int(input("Input first number."))
b = int(input("Input second number."))

sum = a + b
dif = b - a
prod = a * b
quo = a/b
rem = a%b
log = log10(a)
exp = a**b

print("Sum: " + str(sum))
print("Difference: " + str(dif))
print("Product: " + str(prod))
print("Quotient: " + str(quo))
print("Remainder: " + str(rem))
print("log: " + str(log))
print("Raised: " + str(exp))
