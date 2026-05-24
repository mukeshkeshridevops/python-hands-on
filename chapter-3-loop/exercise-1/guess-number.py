import random

guess_number = int(input("Guess a number between 1 to 100:"))
winning_number = random.randint(1, 100)

if guess_number == winning_number:
    print("Congratulations! You guessed the correct number.")
    exit()
elif guess_number < winning_number:
    print("Too low! Try again.")
else:    
    print("Too high! Try again.")  
