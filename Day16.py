#OOP's

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.left(90)
# timmy.left(100)
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.exitonclick())

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_row(["Rourkela","11 sqr","10 million","10mm"])
table.add_row(["Raipur","10 sqr","11 million","20mm"])
table.add_row(["BBSR","12 sqr","12 million","1mm"])
table.add_row(["Gunupur","13 sqr","14 million","5mm"])
print(table)