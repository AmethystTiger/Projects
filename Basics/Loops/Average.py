numbers = input("Enter the values you want to find the average of(End it with 0): ")

total = 0 
no = 0
for i in numbers:
    if int(i) == 0:
        try:
            print(average)
        except:
            print("Start with a number")
    else:
        no += 1
        total += int(i)
        average = total/no
