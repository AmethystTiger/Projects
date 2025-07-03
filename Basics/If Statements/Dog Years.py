
hum_yrs = int(input("Write your age: "))

if hum_yrs < 0:
    print("Please try again with a positive number.")
    quit()
elif 0 < hum_yrs <= 2:
    dog_yrs = hum_yrs * 5.25
    print("You are " + str(dog_yrs) + " years old.")
elif hum_yrs > 2:
    dog_yrs = ((hum_yrs - 2) * 4) + 10.5
    print("You are " + str(dog_yrs) + " years old.")
