from ast import pattern
import re

pattern = re.compile(r'')

while True:
    password = input("Enter Password: ")
    if (len(password)<6):
        print("Password must be atleast 6 characters!")
    elif re.search(r'[!@#$%&_-]', password) is None:
        print('Password must atleast contain one special character!')
    elif re.search(r'\d', password) is None:
        print("Password must atleast contain one numeric character!")
    elif re.search('[A-Z]', password) is None:
        print('Password must atleast contain one Uppercase letter!')
    elif re.match(r'[a-z A-Z 0-9 !@#$%&_-]{6}', password):
        pattern = re.compile(r'[a-z A-Z 0-9 !@#$%&_-]{6}')
        result = pattern.match(password)
        print("Valid Password!")
        break
    else:
        print("Password is invalid!")
        