import math
import unittest
import sys
from types import *
from def_BMI import *
from def_Retirement import *
from def_DistanceFormula import *
from def_EmailVerifier import *

# Import test cases
from Unit_Tests_BMI import *
from Unit_Tests_DistanceFormula import *
from Unit_Tests_EmailVerifier import *
from Unit_Tests_Retirement import *


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


def try_except_with_zero(string):
    while True:
        try:
            value = float(input(string))
            if value < 0:
                print("ERROR: Please enter a value greater than 0!")
                continue
            break
        except ValueError:
            print("ERROR: Please enter a valid numeric value!")

    return value


def main_bmi():
    while True:
        print("\nPlease enter your current height and weight.")
        feet = try_except("  (feet): ")
        inches = try_except_with_zero("(inches): ")
        weight = try_except("(pounds): ")
        bmi = get_bmi(feet, inches, weight)

        print("     BMI:", "%.1f" % bmi)
        if bmi >= 30:
            print("Category: Obese\n")
        elif 25 <= bmi < 30:
            print("Category: Overweight\n")
        elif 18.5 <= bmi < 25:
            print("Category: Normal Weight\n")
        elif bmi < 18.5:
            print("Category: Underweight\n")

        print("Would you like to perform another distance calculation?")
        menu = input("Enter 'y' for yes, otherwise enter anything else to return to the main menu: ")

        if menu != 'y':
            break


def retirement_plan():
    while True:
        age = try_except("\nPlease enter your current age: ")
        annual_salary = try_except("Please enter your current salary: ")
        percentage_saved = try_except("Please enter the percentage saved (as a decimal): ")
        goal = try_except("Please enter your desired goal: ")

        goal_age = retirement(age, annual_salary, percentage_saved, goal)

        if goal_age >= 100:
            print("Sorry, goal not met!\n")
        else:
            print("Your goal will be met at the age of:", int(goal_age), "\n")

        print("Would you like to perform another retirement plan calculation?")
        menu = input("Enter 'y' for yes, otherwise enter anything else to return to the main menu: ")

        if menu != 'y':
            break


def calculate_distance():
    while True:
        x1 = try_except_allow_negative("Please enter a value for x1: ")
        y1 = try_except_allow_negative("Please enter a value for y1: ")
        x2 = try_except_allow_negative("Please enter a value for x2: ")
        y2 = try_except_allow_negative("Please enter a value for y2: ")

        distance = distance_formula(x1, y1, x2, y2)
        print("(", x1, ", ", y1, ") (", x2, ", ", y2, ")")
        print("The distance between the two points: ", "%.2f" % distance, "\n")

        print("Would you like to perform another distance calculation?")
        menu = input("Enter 'y' for yes, otherwise enter anything else to return to the main menu: ")

        if menu != 'y':
            break


def email_verifier():
    while True:
        enteredEmail = str(input('Enter e-mail to be verified: '))
        
        if verifyAtSymbol(enteredEmail) and verifyDotSymbol(enteredEmail) and verifyDomain(enteredEmail) and verifyContent(enteredEmail):
            print(enteredEmail, "is a Valid Email\n")
        else:
            print(enteredEmail, "is an Invalid Email\n")
            
        print("Would you like to verify another email address?")
        menu = input ("Enter 'y' for yes, otherwise enter anything else to return to the main menu: ")
        
        if menu != 'y':
            break


def main():
    while True:
        print('1. Calculate BMI')
        print('2. Calculate Distance Formula')
        print('3. Calculate Retirement')
        print('4. Verify Emails')
        print('5. Run Tests')
        print('Enter anything else to exit.\n')

        choice = (input('Please choose an option: '))

        if choice == '1':
            main_bmi()
            print("")
        elif choice == '2':
            calculate_distance()
            print("")
        elif choice == '3':
            retirement_plan()
            print("")
        elif choice == '4':
            email_verifier()
            print("")
        elif choice == '5':
            unittest.main(exit=False)
        else:
            sys.exit()


if __name__ == '__main__':
    main()
