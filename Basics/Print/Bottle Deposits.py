
one_l = float(input("Enter the number of bottles with less than or equal to 1 litre of capacity: "))
two_l = float(input("Enter the number of bottles with more than 1 litre of capacity: "))

tot_change = (one_l * 0.1) + (two_l * 0.25)
round(tot_change, 2)

print("Your refund is $" + str(tot_change) + ".")
