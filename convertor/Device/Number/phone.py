#1. Number Validation
#2. Number Finder

import os
import phonenumbers
import time

import phonenumbers.carrier
import phonenumbers.geocoder
import phonenumbers.timezone

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

    return valid_number

def national_finder():
    pass


def number_info(number):
    checking = validation(number)
    clearing()

    if checking:
        phoneNumber = phonenumbers.parse(number)
        timeZone = phonenumbers.timezone.time_zones_for_number(phoneNumber)
        Carrier = phonenumbers.carrier.name_for_number(phoneNumber,"en")
        Region = phonenumbers.geocoder.description_for_number(phoneNumber, "en")

        print(f"Phone Number Info\n{phoneNumber}")
        print(f"\nTimezone : {timeZone}")
        print(f"Carrier Service : {Carrier}")
        print(f"Region : {Region}")

def number_matcher():
    pass


def main():
    clearing()
    number = input("> Enter a number: ")
    #check = validation(number)
    number_info(number)
