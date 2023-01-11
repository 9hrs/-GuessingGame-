
import random

# guess the computers random number!

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < random_number:
            print("\033[91m Sorry your guess is too low.")
        elif guess > random_number:
            print("\033[91m Sorry your guess is too high.")

    print(f"\033[91m Congratulations you have guessed the correct number ! ---> {random_number}")

#computer gusses your number 

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could be high as well

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f'Well done the computer has guessed your number --> {guess}, correct! ')

    computer_guess(10)


















