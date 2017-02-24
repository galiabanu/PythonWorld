## CHAPTER 6

## STRING METHODS

spam = 'Hello World!'
spam.lower()

'Hello'.upper().lower()

'abc123'.isalnum()

## Validate input

while True:
    print('What is your age?')
    age = input()
    if age.isdecimal():
        break
    print("Please, enter the number for your age")

    
while True:
    print("Please, enter your new password (letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print("Check your password")