import phonenumbers
from phonenumbers import carrier, geocoder, timezone


Mnumber = input("Enter Mobile Number with country code: ")

Mnumber = phonenumbers.parse(Mnumber)
print(timezone.time_zones_for_number(Mnumber))
print(carrier.name_for_number(Mnumber, 'en'))
print(geocoder.description_for_number(Mnumber, "en"))

print("Valid Mobile Number:", phonenumbers.is_valid_number(Mnumber))
print('Checking possibility of Number:', phonenumbers.is_possible_number(Mnumber))

