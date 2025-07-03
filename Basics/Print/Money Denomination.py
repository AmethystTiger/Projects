cents = int(input("Write the amount of money cents: "))

penny = 1
nickle = 5
dime = 10
quarter = 25
loony = 100
toony = 200

per_toonies = cents//toony
print(str(per_toonies) + " toonies.")
cents = cents % toony

per_loonies = cents//loony
print(str(per_loonies) + " loonies.")
cents = cents % loony

per_quarters = cents//quarter
print(str(per_quarters) + " quarters.")
cents = cents % quarter


per_dime = cents//dime
print(str(per_dime) + " dimes.")
cents = cents % dime

per_nickle = cents//nickle
print(str(per_nickle) + " nickles.")
cents = cents % nickle

per_penny = cents//penny
print(str(per_penny) + " pennies.")
cents = cents % penny

