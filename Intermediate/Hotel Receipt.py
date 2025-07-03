global food_cost
global last_request
global request
global food_cost_list
global food_price
global quantity
global given_mon
global welcome

food_items = ["MENU", "1) Shawarma : QAR7", "2) Chicken Burger : QAR15", "3) Cheese Pizza : QAR5",
              "4) Meat Lovers Pizza : QAR8", "5) Vegan Pizza : QAR7", "6) CheeseBurger : QAR14"]


def yesorno():
    if welcome == "yes":
        req()
    elif welcome == "no":
        print("Then GET OUT!!!!")
        quit()


def hello():
    global welcome
    welcome = input("WELCOME TO *generic hotel name*.\nWould you like to order something?\n")
    yesorno()
    if welcome != "yes" and "no":
        welcome = input("Is that a yes or a no?\n")
        yesorno()


def answer():
    last_request = input("Would you like anything else?(yes/no)\n")
    if last_request == "yes":
        for food in food_items:
            print(food)
        req()
    elif last_request == "no":
        food_price = food_cost
        print("That would be QAR" + str(food_price) + ".")
        due = int(input("Please pay with cash.\n"))
        if due > food_price:
            refund = due - food_price
            print("Your change is QAR" + str(refund) + ".\nThank you for visiting *generic hotel name*.")
        elif due == food_price:
            print("Thank you for visiting *generic hotel name*.")
        elif due < food_price:
            refund = food_price - due
            given_mon = input("Please pay the remaining QAR" + str(refund) + ".\n")
            if given_mon == refund:
                print("THANK YOU")
    elif last_request != "yes" and "no":
        print("Please write a correct response.")
        answer()


food_cost = 0
food_price = 0


def price():
    global food_cost
    global last_request
    global food_price
    global quantity

    if request == "shawarma":
        quantity = int(input("How many of these would you like?\n"))
        food_cost = (7 * quantity) + food_cost
        answer()

    elif request == "chicken burger":
        quantity = int(input("How many of these would you like?\n"))
        food_cost = (15 * quantity) + food_cost
        answer()

    elif request == "cheese pizza":
        quantity = int(input("How many of these would you like?\n"))
        food_cost = (5 * quantity) + food_cost
        answer()

    elif request == "meat lovers pizza":
        quantity = int(input("How many of these would you like?\n"))
        food_cost = (8 * quantity) + food_cost
        answer()

    elif request == "vegan pizza":
        quantity = int(input("How many of these would you like?\n"))
        food_cost = (7 * quantity) + food_cost
        answer()

    elif request == "cheeseburger":
        quantity = int(input("How many of these would you like?\n"))
        food_cost = (14 * quantity) + food_cost
        answer()
    elif request != food_items:
        print("There is no such food item.")
        req()


def req():
    global request
    for food in food_items:
        print(food)
    request = input("Which of the above food items would you like to have?\n")
    price()


hello()

