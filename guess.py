import random


# Function for the user to guess the number
def guess(number):
    random_number = random.randint(1, number)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f"Guess the number between 1 and {number}: "))
        try:    
            if guess_number > random_number:
                print("Too high! Try again.")
            else:
                print("Too low! Try again.")
        except ValueError:
            print("Invalid Input")
    print(f"Congratulations! You guessed it right. The number was {random_number}.")

# Function for the computer to guess the user's number
def computer_guess(number):
    high = number
    low = 1
    feedback = ''
    print("Think of a number and let the computer guess it!")
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could be high b/c low = high

        feedback = input(f"Is {guess} too high(H), too low(L), or correct(C)?? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Invalid Input. Please enter 'H', 'L', or 'C'.")
    print(f"Computer guessed it the number was {guess} ")


# Main Program
try:
    number = int(input("Range of number between 1 to _? "))
    if number <= 1:
        print("Number should be greater then 1.")
    else:
        print("Choose a game mode:")
        print("Press 1: User guessse the number.")
        print("Press 2: Computer guesses your number.")
        choice = int(input("Enter 1 or 2: "))

        if choice == 1:
            guess(number)
        elif choice == 2:
            computer_guess(number)
        else:
            print("Invalid Input. Choose 1 or 2.")
except ValueError:
    print("Invalid Input:")