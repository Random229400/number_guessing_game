import random

# Determines the level (Easy: 10 guesses, Medium: 7 guesses, Hard: 5 guesses)
def levelSelector():
    global guess_amount

    while True:
        print("/=======\\")
        print("| Hard  |\n| Medium|\n| Easy  |")
        print("\\=======/")
        level = input("Choose your difficulty ").capitalize()
        if level == "Hard":
            guess_amount = 5
            break
        elif level == "Medium":
            guess_amount = 7
            break
        elif level == "Easy":
            guess_amount = 10
            break
        else:
            print("Invalid choice!")
    print("====================")
    print(f"{level} mode selected \nYou have {guess_amount} guesses")
    print("Good luck!")

def game(numGuesses, number):
    while True:
        try:
            print("~~~~~~~")
            user_guess = int(input("Guess: "))
        except ValueError:
            print("Invalid number!")
        
        if user_guess < 1 or user_guess > 100:
            print("Stay in the range of 1 - 100")
        else:
            if user_guess == number:
                return numGuesses
            elif user_guess > number:
                print("Guess too high!")
                numGuesses -= 1
            else:
                print("Guess too low!")
                numGuesses -= 1
        if numGuesses == 0:
            return False


def main():
    print("Welcome to my number guessing game!")
    while True:
        print("Guess the number I picked from 1 - 100")
        levelSelector()
        #The number is chosen 
        number = random.randint(1, 100)
        game_state = game(guess_amount, number)
        print("+======================+")
        if not game_state:
            print(f"The number was {number}")
            print("You lose! D:")
        else:
            print(f"The number is {number}")
            print(f"Congrats, you win!🎉, You guessed it in {guess_amount - game_state} turns")

        quit = input("Would you like to quit? Enter q to quit ").lower()

        if quit == "q":
            print("Exiting...")
            break
        else:
            print("Continuing the game...")


if __name__ == "__main__":
    main()
