
accuracy = int(input("Enter the amount of accuracy you want (1-infinity): "))

formoola = 0
total = 0
last_no = 0
for i in range(accuracy):
    if i == 0:
        formoola = 3
        total += formoola
    elif i % 2 == 1:
        first_no = i * 2
        last_no = first_no + 2
        formoola = 4/(first_no*(first_no+1)*last_no)
        total += formoola
    elif i % 2 == 0:
        first_no = i * 2
        last_no = first_no + 2
        formoola = 4/(first_no*(first_no+1)*last_no)
        total -= formoola
    print(total)
