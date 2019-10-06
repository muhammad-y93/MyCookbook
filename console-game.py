while True:
    answer = input("""
    Let's play a game!
    would you like to play? [yes/no]
    """)

    if answer.lower().strip() == "yes":

        answer = input("You've reached a crossroad, would you like to go left or right?").lower().strip()
        if answer == "left":
            answer = input("You encounter a monster, would you like to run or attack").lower().strip()
            if answer == "attack":
                    print("The monster is too big for you, you lost")
            else:
                print("Smart choice, you escaped from the monster")
        elif answer == "right":
            answer = input("You met a beautiful lady, would you like to ask her out? [yes/no]").lower( ).strip( )
            if answer == "yes":
                answer = input("The lady said no, you've been dumped")
            elif answer == "no":
                answer = input("""The lady noticed you, i think she likes yo
                                  Where would you like to take her out?
                                  [Hotel / Park]
                """).lower().strip()
                if answer == "hotel":
                    answer = input("""She said she likes shrimps
                                      Do you have enough money?
                                      [yes / no]
                    """).lower().strip()
                    if answer == "yes":
                        answer = input("You're doing good, have an amazing dinner with her")
                    else:
                        print("You suck, how can you go out with a beautiful lady without money")
            else:
                print("The game is over, you made a wrong choice")
        else:
            print("Invalid choice, you lost")

    else:
        print("That's too bad")
        break
