guess_number = 43
guess = 1
number = int(input("Guess a number between 1 and 100: "))
game_over = False

while not game_over:
    if number < guess_number:
        print("Too low.")
        guess += 1
        number = int(input("Guess again: "))
    elif number > guess_number:
        print("Too high.")
        guess += 1
        number = int(input("Guess again: "))
    else:
        print(f"Congratulations! You guessed the number in {guess} tries.")
        game_over = True