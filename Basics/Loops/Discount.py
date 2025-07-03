
original_price = [4.95, 9.95, 14.95, 19.95, 24.95]
print("OriginalPrice     DiscountAmount          NewPrices")

for p in original_price:
    dis_amt = p * 3/5 + 0.00000001
    round(dis_amt, 2)
    new_amt = p - dis_amt + 0.0000000001
    round(new_amt, 2)
    print("    "+str(p)+"      "+"      "+str(dis_amt)+"      "+"    "+str(new_amt))


