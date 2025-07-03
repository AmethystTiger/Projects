
db_level = int(input("Enter a sound level in decibels: "))

if db_level > 130:
    print("This is louder than a Jackhammer.")
elif db_level == 130:
    print("This is the sound level produced by a Jackhammer.")
elif 130 > db_level > 106:
    print("This is quieter than a Jackhammer but louder than a Gas Lawnmower.")
elif db_level == 106:
    print("This is the sound level produced by a Gas Lawnmower.")
elif 106 > db_level > 70:
    print("This is quieter than a Gas Lawnmower but louder than an Alarm Clock.")
elif db_level == 70:
    print("This is the sound level produced by a Alarm Clock.")
elif 70 > db_level > 40:
    print("This is quieter than a Alarm Clock but louder than a Quiet Room.")
elif db_level == 40:
    print("This is the sound level produced in a Quiet Room.")
elif db_level < 40:
    print("This is quieter than a Quiet Room.")
