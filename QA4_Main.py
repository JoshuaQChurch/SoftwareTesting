import math
import unittest
import sys
from types import *



def try_except(string):
    while True:
        try:
            value = float(input(string))
            break
        except ValueError:
            print("Please insert a valid numeric value!")

    return value




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
            #retirement_plan()
            continue
        elif choice == '4':
            #email_verifier()
            continue
        else:
            sys.exit()


if __name__ == '__main__':
    main()
