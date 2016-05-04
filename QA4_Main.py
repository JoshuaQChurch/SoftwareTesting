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

def retirement_plan():
    age = try_except("\nPlease enter your current age: ")
    annual_salary = try_except("Please enter your current salary: ")
    percentage_saved = try_except("Please enter the percentage saved (as a decimal): ")
    goal = try_except("Please enter your desired goal: ")

    goal_age = retirement(age, annual_salary, percentage_saved, goal)

    if goal_age >= 100:
        print("Sorry, goal not met!")
    else:
        print("Your goal will be met at the age of:", int(goal_age), "\n")



def main():
    while True:
        print('1. Calculate BMI')
        print('2. Calculate Distance Formula')
        print('3. Calculate Retirement')
        print('4. Verify Emails')
        print('Enter anything else to exit.\n')

        choice = (input('Please choose an option: '))

        if choice == '1':
            #main_bmi()
            continue
        elif choice == '2':
            #calculate_distance()
            continue
        elif choice == '3':
            retirement_plan()
            continue
        elif choice == '4':
            #email_verifier()
            continue
        else:
            sys.exit()


if __name__ == '__main__':
    main()
