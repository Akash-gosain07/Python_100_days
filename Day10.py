# def my_function():
#     result =  3*2
#     return result
# output = my_function()
# print(output)
# def format(f_name , l_name):
#     if f_name =="" or l_name=="":
#         return "YOU ARE NOT FOUND"
#     formated_f_name=f_name.title()
#     formated_l_name=l_name
#
#     return f"{formated_f_name} + " f" + {formated_l_name}"
#
# output = format(input("Whats your first name? "),input("Whats your last name? "))
# print(output)
# def is_leap_year(year):
#     """This is a leap year programme and
#     I want to know if it is a leap year"""
#     if year%4==0 and year%100!=0 or year%400==0:
#         return f"{year} is a leap year"
#     else:
#         return f"{year} is not a leap year"
# print(is_leap_year(int(input("enter the year :"))))
# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))

def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2
def divide(num1,num2):
    return num1 / num2

operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    should_accumulate = True
    num1 = float(input("Enter first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter operation symbol: ")
        num2 = float(input("Enter second number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} ={answer} ")

        choice = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start new calculation:  ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()

calculator()
