#1. Number Validation
#2. Number Finder

import os
import phonenumbers
import time

import phonenumbers.carrier
import phonenumbers.geocoder
import phonenumbers.timezone

def clearing():
    os.system("cls" if os.name == 'nt' else "clear")

def validation(number):
    try:
        parsed_number = phonenumbers.parse(number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False

def number_info(number):
    checking = validation(number)
    clearing()

    if checking:
        phoneNumber = phonenumbers.parse(number)
        timeZone = phonenumbers.timezone.time_zones_for_number(phoneNumber)
        Carrier = phonenumbers.carrier.name_for_number(phoneNumber,"en")
        Region = phonenumbers.geocoder.description_for_number(phoneNumber, "en")
        zone = ", ".join(timeZone)        
        
        print(f"Phone Number Info\n{phoneNumber}")
        print(f"\nTimezone : {timeZone}")
        print(f"Carrier Service : {Carrier}")
        print(f"Region : {Region}")
    else:
        print("Invalid phone number format or number is not valid.")


def main():
    clearing()
    number = input("> Enter a number: ")
    number_info(number)
