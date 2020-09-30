from random import randint
comp_guess = randint(1,101)
count = 0
again = 'Y'
prev_count = 0
name = input("Howdy, what's your name? ")
print(f"{name}, I'm thinking of a number between 1 and 100")
print("Try to guess my number.")
guess = 0
# again condition Let Users Play Multiple Rounds and Track Best Scores
while (guess != comp_guess) and (again != 'N'):
    guess = int(input("your guess? "))
    # Limit the Number of Guesses a User Gets
    if (count <= 10):
        if (guess < comp_guess):
            count += 1
            print("Your guess is too low, try again.")
# Limit the Number of Guesses a User Gets
        elif (guess > comp_guess) and (count <= 5):
            count += 1
            print("Your guess is too high, try again.")
        else:    
            count += 1
            prev_Count = count
            if (prev_count < count) and (prev_count > 0):
                print(f"Well done, {name}! You found my number in {prev_count} tries!")
            else:
                print(f"Well done, {name}! You found my number in {count} tries!") 
            guess = 0 
            count = 0
            again = input("Do you want to play again? ").upper()
            comp_guess = randint(1,101)
    # Let Users Play Multiple Rounds and Track Best Scores
    else:
        print("Too many tries...")
        guess = 0 
        count = 0
        again = input("Do you want to play again? ").upper()
        comp_guess = randint(1,101)
