def find_sqrt(num, guess = 1.0):
    if round(guess ** 2, 12) == num:
        return guess
    else:
        g = (guess + (num / guess)) / 2
        return find_sqrt(num, g)
    
number = float(input("Enter the number: "))

print(find_sqrt(number))