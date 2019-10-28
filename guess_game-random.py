import random

user_won = False
correct_answer = random.randint(1, 15)
try:
    while True:
        print("""
                ***********************************
                   Welcome to the guessing game
                ***********************************
                """)
        # print(correct_answer)
        user_guess = int(input("Guess my number: "))

        if user_guess == correct_answer:
            print("You're correct")
            user_won = True
            break
        elif user_guess >= correct_answer:
            print("You guess too high")
        elif user_guess <= correct_answer:
            print("You guess too low")
except ValueError:
    print("Invalid Value")


# if user_won:
#     print("You Won")
# else:
#     print("You loose")