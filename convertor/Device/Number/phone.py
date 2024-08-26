#1. Number Validation
#2. Number Finder

import os
import phonenumbers
import time


options = {
    "Validate" : "Validate The Phone Number",

}

def clearing():
    os.system("cls" if os.name == 'nt' else "clear")

def validation(number):
    phone_number = phonenumbers.parse(number)
    valid_number = phonenumbers.is_valid_number(phone_number)
    valid_possible = phonenumbers.is_possible_number(phone_number)

    print("Validating Number....")
    time.sleep(3)
    if valid_number and valid_possible:
        print(f"\n{number} is a valid number \n{number} is a possible number")
    elif valid_number == False and valid_possible:
        print(f"\n{number} is not a valid number \n{number} is a possible number")
    else:
        print(f"\n{number} is not a valid number \n{number} is not a possible number")

def national_finder():
    pass


def number_info():
    pass


def number_matcher():
    pass


def main():
    clearing()
    number = input("> Enter a number: ")
    validation(number)
