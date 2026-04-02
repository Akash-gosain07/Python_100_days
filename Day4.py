import random
# import my_module
# random_number = random.randint(1,10)
# print(random_number)
# print(my_module.my_favourite_number)
# random_number = random.random() * 10
# print(random_number)
#
# random_float = random.uniform(0,10)
# print(random_float)

# number = random.randint(0,1)
# if number ==0:
#     print('Tail')
# else:
#     print('Head')

# state_of_india = ["Odisha","Bihar","MP","HP"]
# print(state_of_india[1])

# friends=["Alice","Bob","Charlie","David","Emanuel"]
# print(random.choice(friends))

# fruits = ['apple','banana','orange']
# vegetables = ['spinch', 'kale','tomato']
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1])

user = int(input("What do you choose? 0 for rock , 1 for paper , 2 for scissors\n"))
computer = random.randint(0,2)
print(f"Computer chose {computer}")

if user == 0 and computer == 2:
    print("You win!")
elif computer > user:
    print("You lose")
elif computer == user:
    print("Draw")
elif user == 2 and computer == 0:
    print("You lose")
elif user ==1 and computer == 0:
    print("You win")
else:
    print("You typed invalid number. You lose!")


