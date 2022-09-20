from ast import pattern
import re
import json
import phonenumbers
from phonenumbers import geocoder, timezone, carrier
from time import sleep

data = json.loads(open('NetworkPrefixes.json').read())

def main():
    pattern = re.compile(r'[0|0][7-9]\d{9}')
    
    number = input("Enter Mobile Number: ")
    print('\n')
    
    
    rephrase = number[0:4]
    if rephrase in data:
        sleep(1)
        print('Searching for Mobile Number...')
        sleep(2)
        print('Authenticating Mobile Number....')
        sleep(1)
        print("Loading and Reading Retrieved Data...")
        sleep(2)
        print('\n')
        print('Service Provider: ', data[rephrase])
    Phrase = '+234' + number[1:]
    
    MNumber = phonenumbers.parse(Phrase)
    print('Timezone: ', timezone._country_level_time_zones_for_number(MNumber))
    print('Current Location: ', geocoder.description_for_number(MNumber, 'en'))
    print()
    print('Checking possibility of Number:', phonenumbers.is_possible_number(MNumber))
    
    if pattern.match(number):
        print("Valid Mobile Number: True")
        print()
    else:
        print("Valid Mobile Number: False")
    return pattern.match(number)
    


    

if __name__ == '__main__':
    main()