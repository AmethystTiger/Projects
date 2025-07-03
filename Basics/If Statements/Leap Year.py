
year = int(input("Enter a year: "))
by_400 = year % 400
by_100 = year % 100
by_4 = year % 4
if by_400 == 0:
    print(str(year) + " is a leap year.")
else:
    if by_100 == 0:
        print(str(year) + " is not a leap year.")
    else:
        if by_4 == 0:
            print(str(year) + " is a leap year.")
        else:
            print(str(year) + " is not a leap year.")



