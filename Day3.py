# water_level=int(input("Enter the water level: "))
# if water_level >= 80:
#     print("Drain Water")
# else:
#     print("continue")
print("Welcome to the rollercoaster")
height=int(input("Enter your height in cm: "))
age=int(input("Enter your age in years: "))
bill=0
if height >= 120:
    print("You can ride the roller")
    if age <=18 :
        bill=7
        print("Give $7")
    elif age < 12:
        bill=5
        print("Give $5")
    elif age >=45 and age <=55:
        bill+=0
        print("Give $0")
    else:
         bill=12
         print("Give $12")

    wants_photo=input("Do you want ti have a photo take? type y for yes and n for no: ")
    if wants_photo == "y":
        bill+= 3

    print(f"Your total bill is ${bill}")

else:
     print("You can not ride the roller")
#
# n=int(input("Enter a number: "))
# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

# print("welcome to python pizza deliveries!")
# size=input("enter the size of your pizza you want? S, M or L:")
# bill = 0
# if size == "S":
#     bill = 15
#     print("The value of your pizza is",bill)
# elif size == "M":
#     bill = 20
#     print("The value of your pizza is",bill)
# elif size == "L":
#     bill = 25
#     print("The value of your pizza is",bill)
# pepperoni = input("enter the pepperoni of your pizza you want? Y or N:")
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill +=3
#         print("The value of your pizza is", bill)
# extra_cheese = input("enter the extra cheese you want? Y or N:")
# if extra_cheese == "Y":
#     bill += 1
#
#     print(f"Your Pizza total bill is: {bill}")
# else:
#     print("please enter a valid size")
