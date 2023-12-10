import random
import string


def gen_pass(min_len, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += special

    pwd = ''
    meets_criteria = False
    has_number = False
    has_special_char = False

    while not meets_criteria or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special_char = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special_char

    return pwd


min_length = int(input('Enter a minimum length: '))
has_numbers = input('Do you want to have numbers (y/n)?').lower() == "y"
has_special = input('Do you want to have special characters (y/n)?').lower() == "y"
pwd = gen_pass(min_length, has_numbers, has_special)

print(f"The generated password is: {pwd}")
