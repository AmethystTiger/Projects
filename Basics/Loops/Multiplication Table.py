times = int(input("Enter the length of the table: ")) + 1

for i in range(1, times):
    for j in range(1, times):
        print(str(i*j), end=" | ")
    print("\n")
