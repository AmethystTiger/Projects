GPA = {
    "A+":4.0,
    "A":4.0,
    "A-":3.7,
    "B+":3.3,
    "B":3.0,
    "B-":2.7,
    "C+":2.3,
    "C":2.0,
    "C-":1.7,
    "D+":1.3,
    "D":1.0,
    "F":0
       }

n = 0
total = 0
lst = []
in_gpa = input("Enter a grade: ")

while in_gpa != "":
    lst.append(in_gpa)
    in_gpa = input("Enter the remaining grades (blank to quit): ")

for i in lst:
    if i in GPA:
        n += 1
        total += GPA[i]
    else:
        print("Please enter a valid grade.")
        
try:
    print(f"Your average GPA is {total/n}")
except ZeroDivisionError:
    print()
