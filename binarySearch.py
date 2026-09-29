import random

def get_valid_int(message):
    '''
    Asks for a number and checks to see if its a valid integer
    '''
    while True:
        number = input(message)

        if number.isdigit():
            return int(number)

        print("Enter a number: ")

def play_user_rounds(min, max, target):
    '''
    Asks the user to guess the number, and gives a respective answer based on if it's too high, too low, or the right number
    '''
    guesses = 0

    while True:
        guess = get_valid_int("Guess a number: ")
        guesses = guesses + 1

        if guess == target:
            print("Huzzah! You guessed the right number!")
            return guesses

        elif guess < target:
            print("Too low")

        else:
            print("Too high")

def play_cmp_rounds(min, max, target):
    '''
    Computer guesses numbers at random and gets similar answers on high/low
    '''
    guesses = 0
    low = min
    high = max

    while True:
        guess = random.randint(low, high)
        guesses = guesses + 1

        print(f"Computer guessed {guess}")

        if guess == target:
            print("The computer guessed the right number...")
            return guesses

        elif guess < target:
            low = guess + 1

        else:
            high = guess - 1

def print_outcome(user_guesses, comp_guesses):
    '''
    Prints out how many guesses it took the user and computer to guess. It also prints who won and if they tied.
    '''
    print(f"It took you {user_guesses} guesses.")
    print(f"It took the computer {comp_guesses} guesses.")

    if user_guesses < comp_guesses:
        print("You got it quicker than the computer!")
    elif comp_guesses < user_guesses:
        print("The computer got it quicker!")
    else:
        print("You tied!")

def play_again():
    '''
    Asks user if they want to play again and returns True or False.
    '''
    answer = input("Play again? (Y/N): ").strip().upper()

    if answer == "Y":
        return True
    else:
        return False

min = get_valid_int("Enter the minimum number: ")
max = get_valid_int("Enter the maximum number: ")

target = random.randint(min, max)

while True:
    user_guesses = play_user_rounds(min, max, target)
    comp_guesses = play_cmp_rounds(min, max, target)

    print_outcome(user_guesses, comp_guesses)

    if play_again():
        target = random.randint(min, max)
    else:
        print("Bye bye!")
        break