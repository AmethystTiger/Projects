
deposit = float(input("Please write in the amount of money to deposit.\n"))

add_on1 = deposit*4/100
one = add_on1 + deposit
one_year = round(one, 2)

add_on2 = one_year*4/100
two = add_on2 + deposit
two_year = round(two, 2)

add_on3 = two_year*4/100
three = add_on3 + deposit
three_year = round(three, 2)

print("After one year at the rate of 4%, your savings would be " + str(one_year))
print("After two years at the rate of 4%, your savings would be " + str(two_year))
print("After three years at the rate of 4%, your savings would be " + str(three_year))
