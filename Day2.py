# print("Hello"[0])
# print("Hello"[-1])
# print(len("12345"))
# print(type("12345"))
# print(type(123))
# print(type(123.12))
# print(type(True))
# print("Number of letter in your name: " + str( len(input("enter your name: "))))
# print(3*(3+3)/3-3)
# bmi= 65/1.25**2
# print(bmi)
# print(int(bmi))
# print(round(bmi))
# print(round(bmi,2))
# score = 0
# height = 1.8
# is_winning = True
# print(f"Your score is: {score}, your height is: {height},your winning {is_winning}")
print("Welcome to tip calculator")
bill=float(input("What is the total bill ? $"))
tip=int(input("How much tip would you like to give? 10,12, or 15?"))
person=int(input("How many people to split the bill?"))
final = (tip/100 * bill + bill)/person
print("Each person should pay $" + str(round(final,2)))


