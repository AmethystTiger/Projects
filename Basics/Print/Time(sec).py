days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

days = days + (hours / 24) + (minutes / 24 * 60) + (seconds/24 * 3600)
days = round(days, 2)
tot_sec = days * 24 * 60 * 60
tot_sec = round(tot_sec, 2)
days = "{:,}".format(days)
tot_sec = "{:,}".format(tot_sec)

print("The number of seconds in " + str(days) + " days is " + str(tot_sec) + " seconds.")
