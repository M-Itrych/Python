from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = (position + shift_amount) % len(alphabet)
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     return cipher_text
#
# def decrypt(plain_text, shift_amount):
#     return encrypt(plain_text, shift_amount*-1)

def ceasar(start_text, shift_amount, cipher_direction):
    """
    Encodes/Decodes text using Caesar Cipher algorithm
    :param start_text: String
    :param shift_amount: Int
    :param cipher_direction: String
    :return: None
    """
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


run = True

while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasar(text, shift, direction)

    result = input("Type 'yes' if u want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        run = False
        print("Goodbye!")
