# enemies= 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# #Local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
#
# #Global Variable
# health = 10
# def drink_potion():
#     potion_strength = 2
#     print(health)
# drink_potion()

# def prime_number(num):
#     if num==2:
#         return True
#     if num == 1:
#         return False
#     for i in range(2, num):
#         if num% i == 0:
#             return False
#     return True
# print(prime_number(7))

from random import randint
EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(user_guess, actual_guess, turns):
    if user_guess > actual_guess:
        print("Too high")
        return turns - 1
    elif user_guess < actual_guess:
        print("Too low")
        return turns - 1
    else:
        print(f"Correct,{actual_guess}")

def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
    if level == "easy":
         return EASY_LEVEL
    else:
        return HARD_LEVEL
def game():
    print("Welcome to the guessing game!")
    print("I'm thinking of a random number between 1 and 100!")
    answer = randint(1,100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} turns left.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You are out of moves")
            return

game()