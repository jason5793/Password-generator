import random
import string 

def generate_password(min_length,number=True,special_character=True):
    letters=string.ascii_letters
    digit=string.digits
    special=string.punctuation

    character=letters
    if number:
        character+=digit
    if special_character:
        character+=special
    
    pwd=""
    meets_criteria=False
    has_number=False
    has_speical=False

    while not meets_criteria or len(pwd)<min_length:
        new_char=random.choice(character)
        pwd+=new_char
        
        if new_char in digit:
            has_number = True
        elif new_char in special:
            has_speical=True
        
        meets_criteria=True
        if number:
            meets_criteria=+has_number
        if special_character:
            meets_criteria=meets_criteria and has_speical
    return pwd

min_length=int(input("Enter the minimum length:"))
has_number=input("Do you wnat to have a number(y/n)?").lower()=="y"
has_speical=input("Do you wnat to have a special chararcter(y/n)?").lower()=="y"
pwd=generate_password(min_length,has_number,has_speical)
print(f"The generate password is:{pwd}")
