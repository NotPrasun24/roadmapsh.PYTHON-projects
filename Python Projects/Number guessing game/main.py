import random

print("———————" * 5  + "\n Welcome to number guessing game \n" + "———————" *5)
print("\n Game info \n1. In this game you have to guess the number from (1 - 50)")
print("2. The chances you will get to guess the number is based on the level of difficulty")
print("3. Also the game will give you hint wheather your guessed number is lower or higher")

print("———————"*5)


def easy():
    print("———————"*5)
    print("\nGreat, You have decided to go with easy level")
    print("Now you have 5 chance use it wisely. Good Luck!!!\n")
    print("The correct number is between (1-50) ")
    guesses = 5
    number = random.randint(1, 50)
    while guesses > 0:

        try:

            guess = int(input("Enter your guess: "))
            if guess == number:
                print("\nCongralutation, You have won!! ")
                playagain(easy)
                break
            elif guess > 50 or guess < 1:
                print("\nYou have to guess within 1 to 50")
            elif guess < number:
                print("You guessed too low, try guessing higher\n")
                guesses -= 1
                print(f"You have {guesses} guesses left")
            elif guess > number:
                print("You guessed too high, try guessing lower\n")
                guesses -= 1
                print(f"You have {guesses} guesses left")


            if guesses == 0 and guess !=number:
                print("Game Over, You have lost!! The correct answer was " + str(number))
                playagain(easy)
            
        
        except ValueError:
            print("\nPlease enter number, not string")
     

def medium():
    print("———————"*5)
    print("\nGreat, You have decided to go with Medium level")
    print("Now you have 3 chance use it wisely. Good Luck!!!\n")
    print("The correct number is between (1-50) ")
    guesses = 3
    number = random.randint(1,50)
    while guesses > 0:
        try:

            guess = int(input("Enter your guess: "))
            if guess == number:
                print("\nCongralutation you have won!\n")
                playagain(medium)
                break
            elif guess > 50 or guess < 1:
                print("\nYou have to guess between 1 to 50 ")
            elif guess > number:
                print("You guessed too high, try guessing lower\n")
                guesses -= 1
                print(f"You have {guesses} left now")
            elif guess < number:
                print("You guessed too low, try guessing higher\n")
                guesses -= 1
                print(f"You have {guesses} left now")
            if guesses == 0 and guess != number:
                print("\n GAMES OVER, You have lost!! The correct answer was " + str(number))
                playagain(medium)
        except ValueError:
            print("\nPlease enter number, not string")
        

def difficult():
    
    print("———————"*5)
    print("\nGreat, You have decided to go with Difficult level")
    print("Now you have 3 chance use it wisely. Good Luck!!!\n")
    print("The correct number is between (1-50) ")
    guesses = 1
    number = random.randint(1,50)
    while guesses > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess > 50 or guess < 1:
                print("\nSorry, You have to guess between 1 to 50 \n")
            elif guess == number:
                print("\nCongralutations, You have won the Hardest level of all\n")
                playagain(difficult)
            elif guess > number:
                guesses -= 1
            elif guess < number:
                guesses -= 1
            if guesses == 0 :
                print("\nGAMES OVER, You have lost!! The correct answer was " + str(number))
                playagain(difficult)
        except ValueError:
            print("\nPlease enter number, not string")


def playagain(level_function):
    print("\nPress 1 to try again \nOr press 2 to exit the game!")
    again = input("What would you like to do: ")
    if again == "1":
        level_function()
    elif again == "2":
        print("Thanks for playing the game!!")
        print("———————"*5)

        gamemenu()
    else:
        print("Please enter the correct number!")
        playagain(level_function)



    
def gamemenu():

    print("Please select the difficulty level: ")
    print("1. Easy level (5 chances)")
    print("2. Medium level (3 chances)")
    print("3. difficult levle (1 chance)")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            easy()
        elif choice == 2:
            medium()
        elif choice == 3:
            difficult()

        else:
            print("PLEASE ENTER CORRECT NUMBER")
            gamemenu()
    except ValueError:
        print("PLEASE ENTER A NUMBER NOT STRINGS\n")
        gamemenu()

gamemenu()
