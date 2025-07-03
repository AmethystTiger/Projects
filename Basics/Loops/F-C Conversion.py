print("Celsius        Farenheit")
c = 00
f = 0
for i in range(0, 100, 10):
    c = i
    f = (c * 9/5) + 32
    print("   "+str(c)+"            "+str(round(f, 2))+"    ")
