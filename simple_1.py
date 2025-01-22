# basic arithmetic operations

def calculator(num1, num2, cal = "add"):
    value = 0
    if cal == "add":
        add = num1 + num2
        value = add
    elif cal == "sub":
        sub = num1 - num2
        value = sub
    elif cal == "div":
        div = num1/num2
        value = div
    elif cal == "mul":
        mul = num1 * num2
        value = mul
    return value

# num1 = float(input("Insert first number="))
# num2 = float(input("Insert second number="))
# cal = str(input(""))
# print(calculator(num1, num2, cal))

##############################################################################################################################

# function to swap values of variables

def swap(ele1, ele2):
    ele1,ele2 = ele2,ele1
    return ele1, ele2
# print(swap(34, 45))

###############################################################################################################################

# To generate random numbers
import random

def random_num(s, e):
    num = random.randint(s,e)
    return num

# print(random_num(20,40))

###################################################################################################################################

import calendar

def month_calender(m,y):
    cal = calendar.TextCalendar().formatmonth(int(y), int(m))
    return cal

# print(month_calender(1,2025))

###################################################################################################################################
# Write a Python program to solve quadratic equation.
import math

def quadratic(a,b,c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    # Check if the discriminant is positive, negative, or zero
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2*a)
        print(f"Root: {root}")
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")

# quadratic(1,2,3)

##########################################################################################################

