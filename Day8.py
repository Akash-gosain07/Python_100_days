# def greet(name):
#     print("Welcome " + name)
#     print(f"how are yu doing {name}?")
#
# greet("akash")
import string

# def greet_with(name, location):
#     print(f"Hello {name}, you are from {location}")
# greet_with("Akash","Odisha")
# greet_with(location="odisha",name="akash")

# def love_count(name1,name2):
#     combine_names = name1 + name2
#     lower_name = combine_names.lower()
#
#     t = lower_name.count("t")
#     r = lower_name.count("r")
#     u =lower_name.count("u")
#     e =lower_name.count("e")
#     first_digit = t + r+ u+e
#
#     l = lower_name.count("l")
#     o = lower_name.count("o")
#     v = lower_name.count("v")
#     e = lower_name.count("e")
#     second_digit = l + o + v + e
#
#     score=int(str(first_digit)+str(second_digit))
#     print(score)
# love_count("Sujeet","Das")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
text = input("Type your message:\n ").lower()
shift = int(input("Type the shift number:\n "))
alphabet = string.ascii_letters
if direction == 'encode':
    def encrypt(original_text , shift_amount):
        cipher_text = ""
        for letter in original_text:
            shift_position=alphabet.index(letter) + shift_amount
            if letter not in alphabet:
                original_text += letter
            else:
                shift_position=shift_position % 26
                cipher_text+=alphabet[shift_position]

        print(f"The encrypted text is: {cipher_text}")
    encrypt(original_text=text,shift_amount=shift)
else:
    def decrypt(original_text , shift_amount):
        ciper_text = ""
        for letter in original_text:
            shift_position=alphabet.index(letter) - shift_amount
            if letter not in alphabet:
                original_text += letter
            else:
                shift_position=shift_position % 26
                ciper_text+=alphabet[shift_position]
        print(f"The decrypted text is: {ciper_text}")
    decrypt(original_text=text,shift_amount=shift)