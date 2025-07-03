
min = int(input("Enter the number of minutes: "))
txt = int(input("Enter the number of texts: "))

more_min_50 = min - 50
more_txt_50 = txt - 50
extra_min = (min - 50) * 0.25
extra_txt = (txt - 50) * 0.15
additional = 0.44
taxation = (additional + 15) * 5/100
taxation = round(taxation, 2)
tooots = 15 + taxation + additional
print("Base amount = $15")

if more_min_50 > 0 and more_txt_50 > 0:
    print("Extra cost = $" + str(extra_min + extra_txt))
elif more_min_50 > 0:
    print("Extra cost = $" + str(extra_min))
elif more_txt_50 > 0:
    print("Extra cost = $" + str(extra_txt))

print("911 fee = $0.44")

if more_min_50 > 0 and more_txt_50 > 0:
    tax = (extra_txt + extra_min + 15 + additional) * 5/100
    tax = round(tax, 2)
    print("Tax amount = $" + str(tax))
    total = extra_txt + extra_min + 15 + additional + tax
    print("Total amount = $" + str(total))
elif more_min_50 > 0:
    tax = (extra_min + 15 + additional) * 5/100
    tax = round(tax, 2)
    print("Tax amount = $" + str(tax))
    total = extra_min + 15 + additional + tax
    print("Total amount = $" + str(total))
elif more_txt_50 > 0:
    tax = (extra_txt + 15 + additional) * 5/100
    tax = round(tax, 2)
    print("Tax amount = $" + str(tax))
    total = extra_txt + 15 + additional + tax
    print("Total amount = $" + str(total))
else:
    print("Tax amount = $" + str(taxation))
    print("Total amount = $" + str(tooots))

