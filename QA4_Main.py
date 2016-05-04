import math
import unittest
import sys
from types import *
from def_BMI import *
from def_Retirement import *
from def_DistanceFormula import *
from def_EmailVerifier import *


def try_except(string):
    while True:
        try:
            value = float(input(string))
            if value <= 0:
                print("ERROR: Please enter a value greater than 0!")
                continue
            break
        except ValueError:
            print("ERROR: Please enter a valid numeric value!")

    return value


def try_except_allow_negative(string):
    while True:
        try:
            value = float(input(string))
            break
        except ValueError:
            print("ERROR: Please enter a valid numeric value!")

    return value


def main_bmi():
    print("\nPlease enter your current height and weight.")
    feet = try_except("  (feet): ")
    inches = try_except("(inches): ")
    weight = try_except("(pounds): ")
    bmi = get_bmi(feet, inches, weight)

    print("     BMI:", "%.1f" % bmi)
    if bmi >= 30:
        print("Category: Obese")
    elif 25 <= bmi < 30:
        print("Category: Overweight")
    elif 18.5 <= bmi < 25:
        print("Category: Normal Weight")
    elif bmi < 18.5:
        print("Category: Underweight")
    print("")


def retirement_plan():
    age = try_except("\nPlease enter your current age: ")
    annual_salary = try_except("Please enter your current salary: ")
    percentage_saved = try_except("Please enter the percentage saved (as a decimal): ")
    goal = try_except("Please enter your desired goal: ")

    goal_age = retirement(age, annual_salary, percentage_saved, goal)

    if goal_age >= 100:
        print("Sorry, goal not met!\n")
    else:
        print("Your goal will be met at the age of:", int(goal_age), "\n")


def calculate_distance():
    x1 = try_except_allow_negative("Please enter a value for x1: ")
    y1 = try_except_allow_negative("Please enter a value for y1: ")
    x2 = try_except_allow_negative("Please enter a value for x2: ")
    y2 = try_except_allow_negative("Please enter a value for y2: ")

    distance = distance_formula(x1, y1, x2, y2)
    print("The distance is: ", "%.2f" % distance)
    print("")


def email_verifier():
    while True:
        enteredEmail = str(input('Enter e-mail to be verified: '))
        
        if verifyAtSymbol(enteredEmail) and verifyDotSymbol(enteredEmail) and verifyDomain(enteredEmail) and verifyContent(enteredEmail):
            print(enteredEmail, "is a Valid Email\n")
        else:
            print(enteredEmail, "is an Invalid Email\n")
            
        print("Would you like to verify another email address?")
        emailMenu = input ("Enter 'y' for yes, otherwise enter anything else to return to the main menu: ")
        
        if (emailMenu != 'y'):
            break


def main():
    while True:
        print('1. Calculate BMI')
        print('2. Calculate Distance Formula')
        print('3. Calculate Retirement')
        print('4. Verify Emails')
        print('Enter anything else to exit.\n')

        choice = (input('Please choose an option: '))

        if choice == '1':
            main_bmi()
            continue
        elif choice == '2':
            calculate_distance()
            continue
        elif choice == '3':
            retirement_plan()
        elif choice == '4':
            email_verifier()
        else:
            sys.exit()


if __name__ == '__main__':
    main()
