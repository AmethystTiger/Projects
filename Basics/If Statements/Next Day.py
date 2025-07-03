year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))


if year % 4 == 0:
    if month == 2:
        if day in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28):
            day = day + 1
            print(str(day) + "-2-" + str(year))
        elif day == 29:
            month = 3
            day = 1
            print(str(day) + "-" + str(month) + "-" + str(year))
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        if day in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30):
            day = day + 1
            print(str(day) + "-" + str(month) + "-" + str(year))
        elif day == 31:
            month = month + 1
            day = 1
            print(str(day) + "-" + str(month) + "-" + str(year))
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29):
            day = day + 1
            print(str(day) + "-" + str(month) + "-" + str(year))
        elif day == 30:
            month = month + 1
            day = 1
            print(str(day) + "-" + str(month) + "-" + str(year))
    elif month == 12:
        if day in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30):
            day = day + 1
            print(str(day) + "-" + str(month) + "-" + str(year))
        elif day == 31:
            year = year + 1
            month = 1
            day = 1
            print(str(day) + "-" + str(month) + "-" + str(year))


else:
    if month == 2:
        if day in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27):
            day = day + 1
            print(str(day) + "-2-" + str(year))
        elif day == 28:
            month = 3
            day = 1
            print(str(day) + "-" + str(month) + "-" + str(year))
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        if day in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30):
            day = day + 1
            print(str(day) + "-" + str(month) + "-" + str(year))
        elif day == 31:
            month = month + 1
            day = 1
            print(str(day) + "-" + str(month) + "-" + str(year))
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29):
            day = day + 1
            print(str(day) + "-" + str(month) + "-" + str(year))
        elif day == 30:
            month = month + 1
            day = 1
            print(str(day) + "-" + str(month) + "-" + str(year))
    elif month == 12:
        if day in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30):
            day = day + 1
            print(str(day) + "-" + str(month) + "-" + str(year))
        elif day == 31:
            year = year + 1
            month = 1
            day = 1
            print(str(day) + "-" + str(month) + "-" + str(year))



