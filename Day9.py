# colour = {"Apple":"Red",
#           "Banana":"Yellow",
#           "Pear":"Green"
#           }
# print(colour["Pear"])
#
# colour["peach"] = "pink"
# print(colour["peach"])
# print(colour)
#
# my_empty_dictionary = {}
#
# colour["Apple"]="Green"
# for key in colour:
#     print(key)
#     print(colour[key])
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {
#     'Harry' : "Exceeds Expectations",
#     "Ron":"Acceptable",
#     "Hermione":"Outstanding",
#     "Draco":"Acceptable",
#     "Neville":"Fail"
# }
# for student in student_grades:
#     print(student_grades[student])

# capitals={
#     "france":"paris",
#     "germany":"berlin",
# }
#
# travel_log = {
#     "france":{
#         "num_times_visited":8,
#         "Cities_visited":["Paris", "Lille", "Dijon"]
#     },
#     "germany":["stuttgart","berlin"],
# }
#
# print(travel_log["france"]["Cities_visited"][1])
#
# nested_list =["A","B",["C","D"]]
# print(nested_list[2][1])
def highest(bidding):
    winner = ""
    highest_bid = 0
    for bidder in bidding:
        if bidding[bidder] > highest_bid:
            highest_bid = bidding[bidder]
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")
name=input("What is your name?")
bid = int(input("What is your bid?: $"))
blind_bid={
    name:bid
}
ask=input("Is their any other bidder? Yes or NO ")
while ask != "no":
    name = input("What is your name?")
    bid = int(input("What is your bid?: $"))
    blind_bid = {
        name: bid
    }
    ask = input("Is their any other bidder? Yes or NO ").lower()
    if ask == "no":
        ask = False
        highest(blind_bid)
    elif ask == "yes":
        print("\n"*20)
