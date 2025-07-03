global pos_int


def ifornot():
    if pos_int < 0:
        inte()
    else:
        somebody = (pos_int*(pos_int + 1))/2

        print("The sum of the first n positive number is " + str(somebody))


def inte():
    global pos_int
    pos_int = int(input("Write a positive integer 'n': "))
    ifornot()


inte()




