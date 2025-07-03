from tkinter import *
from operator import add, mul, sub, truediv, mod
from math import pow

# Defining the layout
root = Tk()
root.geometry("210x335")
root.title("Calculator")
root.iconbitmap("calculator.ico")

# Function to simplify the button defining process
def simple_buttons(master, txt, cmd, *args):
    return Button(master, text=txt, command=lambda: cmd(*args))

def convert(w1, val1, w2, entry):
    conv = w1 + "-" + w2
    convopp = w2 + "-" + w1
    entry.delete(0, END)
    try:
        if conv in conversion_chart:
            entry.insert(0, round(val1 * conversion_chart[conv], 6))
        else:
            entry.insert(0, round(val1 * (1 / conversion_chart[convopp]), 6))
    except ValueError:
        return

conversion_chart = {# Mass Conversion
                    "Kg-Kg":1, "Kg-G":1000, "Kg-Mg":100000, "Kg-Ounce":35.273962,
                    "Kg-Pound": 2.204623, "Kg-Stone": 1/6.35, "Kg-UK Ton": 1/1016,
                    "Kg-US Ton": 1/907, "Kg-Metric Ton": 1/1000,

                    "G-G":1, "G-Mg":100, "G-Ounce":1/28.35,
                    "G-Pound": 1/454, "G-Stone": 1/6350, "G-UK Ton": 1/1016000,
                    "G-US Ton": 1/907185, "G-Metric Ton": 1/1000000,

                    "Mg-Mg":1, "Mg-Ounce":1/28350,
                    "Mg-Pound": 1/453592, "Mg-Stone": 1/6350000, "Mg-UK Ton": 1/1016000000,
                    "Mg-US Ton": 1/9072000000, "Mg-Metric Ton": 1/1000000000,

                    "Ounce-Ounce":1, "Ounce-Pound": 1/16, "Ounce-Stone": 1/224,
                    "Ounce-UK Ton": 1/35840, "Ounce-US Ton": 1/32000, "Ounce-Metric Ton": 1/35274,

                    "Pound-Pound": 1, "Pound-Stone": 1/14, "Pound-UK Ton": 1/2240,
                    "Pound-US Ton": 1/2000, "Pound-Metric Ton": 1/2205,

                    "Stone-Stone": 1, "Stone-UK Ton": 1/160,
                    "Stone-US Ton": 1/143, "Stone-Metric Ton": 1/157,

                    "UK Ton-UK Ton": 1, "UK Ton-US Ton": 1/1.12, "UK Ton-Metric Ton": 1/1.02,

                    "US Ton-US Ton": 1, "US Ton-Metric Ton": 1/1.102,

                    "Metric Ton-Metric Ton": 1,

                    # Length Conversion
                    "Km-Km":1, "Km-M":1000, "Km-Cm":100000, "Km-Mm":1000000, "Km-Micro":1000000000,
                    "Km-Nano":1000000000000, "Km-Mile":1/1.609, "Km-Yard":1094, "Km-Foot":3281,
                    "Km-Inch":39370,"Km-Nautical Mile":1/1.852,

                    "M-M":1, "M-Cm":100, "M-Mm":1000, "M-Micro":1000000,
                    "M-Nano":1000000000, "M-Mile":1/1609, "M-Yard":1.094, "M-Foot":3.281,
                    "M-Inch":39.370,"M-Nautical Mile":1/1852,

                    "Cm-Cm":1, "Cm-Mm":10, "Cm-Micro":10000,
                    "Cm-Nano":10000000, "Cm-Mile":1/160934, "Cm-Yard":1/91.44, "Cm-Foot":1/30.48,
                    "Cm-Inch":1/2.54,"Cm-Nautical Mile":1/185200,

                    "Mm-Mm":1, "Mm-Micro":1000,
                    "Mm-Nano":1000000, "Mm-Mile":1/1609340, "Mm-Yard":1/914, "Mm-Foot":1/305,
                    "Mm-Inch":1/25.4,"Mm-Nautical Mile":1/1852000,

                    "Micro-Micro":1,
                    "Micro-Nano":1000, "Micro-Mile":1/1609340000, "Micro-Yard":1/914400, "Micro-Foot":1/304800,
                    "Micro-Inch":1/25400,"Micro-Nautical Mile":1/1.852e+9,

                    "Nano-Nano":1, "Nano-Mile":1/1.609e+12, "Nano-Yard":1/9.144e+8, "Nano-Foot":1/3.048e+8,
                    "Nano-Inch":1/2.54e+7,"Nano-Nautical Mile":1/1.852e+12,

                    "Mile-Mile":1, "Mile-Yard":1760, "Mile-Foot":5280,
                    "Mile-Inch":63360,"Mile-Nautical Mile":1/1.151,

                    "Yard-Yard":1, "Yard-Foot":3,
                    "Yard-Inch":36,"Yard-Nautical Mile":1/2025,

                    "Foot-Foot":1,
                    "Foot-Inch":12,"Foot-Nautical Mile":1/6076,

                    "Inch-Inch":1,"Inch-Nautical Mile":1/72913,

                    "Nautical Mile-Nautical Mile":1,

                   }

"""Start of all calculator functions"""
# Dictionary containing different operations
ops = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":truediv,
    "^":pow,
    "%":mod
        }

# Function to check if the number is a float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Function to calculate and show the final answer
def result(num):
    calculator_entry.delete(0, END)
    # Check if the num is a float
    if num.isdigit()|isfloat(num):
        return float(num)
    for i in ops.keys():                                # Goes through all operations
        left, operation, right = num.partition(i)       # Divides the num into three (could give a blank)
        if operation in ops:                            # Checks if the current operation is in the ops list
            try:
                return ops[operation](result(left), result(right))
            except TypeError:
                return ops[operation](result("0"), result(right))

# Function to display a single number
def show(num):
    calculator_entry.insert(END, num)

# Function to clear the calculator
def clear():
    calculator_entry.delete(0, END)

# Function to remove the last character
def remove():
    calculator_entry.delete(len(calculator_entry.get())-1, END)

# Creating the buttons within the calculator
calculator_entry = Entry(root, borderwidth=3)

b1 = simple_buttons(root, "1", show, 1)
b2 = simple_buttons(root, "2", show, 2)
b3 = simple_buttons(root, "3", show, 3)
b4 = simple_buttons(root, "4", show, 4)
b5 = simple_buttons(root, "5", show, 5)
b6 = simple_buttons(root, "6", show, 6)
b7 = simple_buttons(root, "7", show, 7)
b8 = simple_buttons(root, "8", show, 8)
b9 = simple_buttons(root, "9", show, 9)
b0 = simple_buttons(root, "0", show, 0)

bdot = simple_buttons(root, ".", show, ".")
bpow = simple_buttons(root, "^", show, "^")
badd = simple_buttons(root, "+", show, "+")
bsub = simple_buttons(root, "-", show, "-")
bdiv = simple_buttons(root, "/", show, "/")
bmul = simple_buttons(root, "*", show, "*")

bcle = simple_buttons(root, "AC", clear)
bent = Button(root, text="Enter", command=lambda: show(result(calculator_entry.get())))
bdel = simple_buttons(root, "Remove", remove)

placing_list_calc = [[calculator_entry, 5, 35, 200, 40],
               [b1, 5, 80, 50, 50], [b2, 55, 80, 50, 50], [b3, 105, 80, 50, 50], [badd, 155, 80, 50, 50],
               [b4, 5, 130, 50, 50], [b5, 55, 130, 50, 50], [b6, 105, 130, 50, 50], [bsub, 155, 130, 50, 50],
               [b7, 5, 180, 50, 50], [b8, 55, 180, 50, 50], [b9, 105, 180, 50, 50], [bdiv, 155, 180, 50, 50],
               [b0, 5, 230, 50, 50], [bdot, 55, 230, 50, 50], [bpow, 105, 230, 50, 50], [bmul, 155, 230, 50, 50],
               [bent, 5, 280, 100, 50], [bcle, 105, 280, 50, 50], [bdel, 155, 280, 50, 50]]

def create_calculator_gui():
    root.geometry("210x335")
    for i in range(len(placing_list_calc)):
        index = placing_list_calc[i]
        index[0].place(x=index[1], y=index[2], width=index[3], height=index[4])
def delete_calculator_gui():
    for i in range(len(placing_list_calc)):
        index = placing_list_calc[i]
        index[0].place_forget()
"""End of all calculator functions"""


"""Start of all Mass Conversion functions"""

mass_conversion_values = ["Kg", "G", "Mg", "Ounce",
                     "Pound", "Stone", "UK Ton",
                     "US Ton", "Metric Ton"]
def mass_current1(event):
    mass_option1.set(event)
def mass_current2(event):
    mass_option2.set(event)

mass_option1 = StringVar()
mass_option1.set(mass_conversion_values[0])
mass_option2 = StringVar()
mass_option2.set(mass_conversion_values[0])

# Creating the buttons within the conversion
mass_list1 = OptionMenu(root, mass_option1, *mass_conversion_values, command=mass_current1)
mass_list2 = OptionMenu(root, mass_option2, *mass_conversion_values, command=mass_current2)
mass_to = Label(root, text="To")
mass_entry1 = Entry(root)
mass_entry2 = Entry(root)
bres = Button(root, text="Calculate", command=lambda: convert(mass_option1.get(), float(mass_entry1.get()),
                                                              mass_option2.get(), mass_entry2))

placing_list_m_con = [[mass_list1, 5, 75, 95, 30], [mass_list2, 5, 150, 95, 30], [mass_entry1, 100, 75, 95, 30],
                      [mass_entry2, 100, 150, 95, 30], [bres, 75, 200, 60, 30]]

def create_m_con_gui():
    root.geometry("210x260")
    for i in range(len(placing_list_m_con)):
        index = placing_list_m_con[i]
        index[0].place(x=index[1], y=index[2], width=index[3], height=index[4])
    mass_to.place(x=50, y=114, width=50, height=30, anchor=N)
def delete_m_con_gui():
    for i in range(len(placing_list_m_con)):
        index = placing_list_m_con[i]
        index[0].place_forget()
    mass_to.place_forget()
"""End of all Mass Conversion functions"""


"""Start of all Length Conversion functions"""

length_conversion_values = ["Km", "M", "Cm", "Mm", "Micro", "Nano", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"]
def length_current1(event):
    length_option1.set(event)
def length_current2(event):
    length_option2.set(event)

length_option1 = StringVar()
length_option1.set(length_conversion_values[0])
length_option2 = StringVar()
length_option2.set(length_conversion_values[0])

# Creating the buttons within the conversion
length_list1 = OptionMenu(root, length_option1, *length_conversion_values, command=length_current1)
length_list2 = OptionMenu(root, length_option2, *length_conversion_values, command=length_current2)
length_to = Label(root, text="To")
length_entry1 = Entry(root)
length_entry2 = Entry(root)
bres = Button(root, text="Calculate", command=lambda: convert(length_option1.get(), float(length_entry1.get()),
                                                              length_option2.get(), length_entry2))

placing_list_l_con = [[length_list1, 5, 75, 95, 30], [length_list2, 5, 150, 95, 30], [length_entry1, 100, 75, 95, 30],
                      [length_entry2, 100, 150, 95, 30], [bres, 75, 200, 60, 30]]
def create_l_con_gui():
    root.geometry("210x260")
    for i in range(len(placing_list_l_con)):
        index = placing_list_l_con[i]
        index[0].place(x=index[1], y=index[2], width=index[3], height=index[4])
    length_to.place(x=50, y=114, width=50, height=30, anchor=N)
def delete_l_con_gui():
    for i in range(len(placing_list_l_con)):
        index = placing_list_l_con[i]
        index[0].place_forget()
    length_to.place_forget()
"""End of all Length Conversion functions"""


"""Start of all Temperature Conversion functions"""
'''temp_conversion_chart = {   "Fahrenheit-Fahrenheit":1, "Fahrenheit-Celsius":(0°F − 32) × 5/9,
                            "Fahrenheit-Kelvin":(0°F − 32) × 5/9 + 273.15,
                            "Celsius-Celsius":1, "Celcius-Kelvin":0°C + 273.15, "Kelvin-Kelvin":1}'''
temp_conversion_values = ["Fahrenheit", "Celsius", "Kelvin"]
def temp_current1(event):
    temp_option1.set(event)
def temp_current2(event):
    temp_option2.set(event)

def temp_convert(w1, num, w2):
    conv = w1 + "-" + w2
    total = 0

    if conv == ("Fahrenheit-Fahrenheit" or "Celsius-Celsius" or "Kelvin-Kelvin"):
        total = num
    elif conv == "Fahrenheit-Celsius":
        total = (num - 32) * 5 / 9
    elif conv == "Fahrenheit-Kelvin":
        total = ((num - 32) * 5/9) + 273.15
    elif conv == "Celsius-Fahrenheit":
        total = (num * 9 / 5) + 32
    elif conv == "Celsius-Kelvin":
        total = num + 273.15
    elif conv == "Kelvin-Fahrenheit":
        total = ((num - 273.15) * 9 / 5 ) + 32#(num − 273.15) * 9/5 + 32
    elif conv == "Kelvin-Celsius":
        total = num - 273.15

    temp_entry2.delete(0, END)
    temp_entry2.insert(0, round(total, 6))

temp_option1 = StringVar()
temp_option1.set(temp_conversion_values[0])
temp_option2 = StringVar()
temp_option2.set(temp_conversion_values[0])

# Creating the buttons within the conversion
temp_list1 = OptionMenu(root, temp_option1, *temp_conversion_values, command=temp_current1)
temp_list2 = OptionMenu(root, temp_option2, *temp_conversion_values, command=temp_current2)
temp_to = Label(root, text="To")
temp_entry1 = Entry(root)
temp_entry2 = Entry(root)
bres = Button(root, text="Calculate", command=lambda: temp_convert(temp_option1.get(), float(temp_entry1.get()),
                                                              temp_option2.get()))

placing_list_t_con = [[temp_list1, 5, 75, 95, 30], [temp_list2, 5, 150, 95, 30], [temp_entry1, 100, 75, 95, 30],
                      [temp_entry2, 100, 150, 95, 30], [bres, 75, 200, 60, 30]]
def create_t_con_gui():
    root.geometry("210x260")
    for i in range(len(placing_list_t_con)):
        index = placing_list_t_con[i]
        index[0].place(x=index[1], y=index[2], width=index[3], height=index[4])
    temp_to.place(x=50, y=114, width=50, height=30, anchor=N)
def delete_t_con_gui():
    for i in range(len(placing_list_t_con)):
        index = placing_list_t_con[i]
        index[0].place_forget()
    temp_to.place_forget()
"""End of all Temperature Conversion functions"""


def calculator():
    delete_l_con_gui()
    delete_m_con_gui()
    delete_t_con_gui()
    create_calculator_gui()
def mass_conversion():
    delete_calculator_gui()
    delete_l_con_gui()
    delete_t_con_gui()
    create_m_con_gui()
def length_conversion():
    delete_calculator_gui()
    delete_m_con_gui()
    delete_t_con_gui()
    create_l_con_gui()
def temperature_conversion():
    delete_calculator_gui()
    delete_m_con_gui()
    delete_l_con_gui()
    create_t_con_gui()

def main(event = 1):
    if clicked.get() == "Calculator":
        calculator()
    elif clicked.get() == "Conversion(Mass)":
        mass_conversion()
    elif clicked.get() == "Conversion(Length)":
        length_conversion()
    elif clicked.get() == "Conversion(Temp)":
        temperature_conversion()
    return event

# Creating the drop-down menu
options = [
    "Calculator",
    "Conversion(Mass)",
    "Conversion(Length)",
    "Conversion(Temp)"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=main)
drop.place(x=105, y=3, width=150, height=30, anchor=N)

main()
# Creating the main loop
root.mainloop()
