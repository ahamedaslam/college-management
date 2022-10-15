name = input("Type your name: ")
print("Hey!", name, "welcome to this Adventures.")

answer = input("woops. you are on dirt road.which way you would like to go left or right? ").lower()
if answer == "left":
        answer = input("Now you are on a river, you walk around it or swim across?. Type you wanna walk or swim across: ")

        if answer == "swim":
            print("You swam across many miles and you were eaten by an alligator!!")

        elif answer == "walk":
            print("You walked out for many miles and ran out of water and you lost the game")
        else:
            print("Not a valid option.You lose.")
elif answer == "right":
        answer = input("You came to a bridge and it looks woobly!. Do you want to take (back/cross)? ")
        if answer == "back":
            print("You go back and lose.")

        elif answer == "cross":
            answer = input("You cross the bridge and meet a stranger. Do you want to talk to them (yes/no)? ")
            if answer == "yes":
                print("You talk talk to the stranger and they give you a gold. You win!!")
            elif answer == "no":
                print("You ignore the stranger and you lose the game.")
            else:
                print("Not a valid option.You lose.")
        else:
            print("Not a valid option.You lose.")
else:
    print("Not a valid option.You lose")
    print("Thank you for trying", name)