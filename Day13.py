# def my_function():
#     for i in range(0, 21):
#         if i == 20:
#             print("You got i")
# my_function()

# from random import randint
# dic_images = ['1', '2', '3', '4', '5', '6']
# dic_num = randint(0,5)
# print(dic_images[dic_num])

# year = int(input("what's your year of birth? "))
#
# if 1980 <  year < 1994:
#     print("You are millennial")
# elif year >= 1994:
#     print("You are Gen-z ")
try:
    age = int(input("What is your age? "))
except ValueError:
    print("Sorry, you didn't enter a number.")
    age = int(input("What is your age? "))
if age > 18:
    print(f"You can drive {age}")
else:
    print("You can not drive")