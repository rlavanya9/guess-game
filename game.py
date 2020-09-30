from random import randint
comp_guess = randint(1,101)
count = 0
name = input("Howdy, what's your name?")
print(f'''{name},I'm thinking of a number between 1 and 100''')
print("Try to guess my number.")
guess = 0
while (guess != comp_guess):
    print(comp_guess)
    guess = int(input("your guess?"))
    if (guess < comp_guess):
        count += 1
        print("Your guess is too low, try again.")
    elif (guess > comp_guess):
        count += 1
        print("Your guess is too high, try again.")
    else:
        count += 1
        print(f"Well done, {name}! You found my number in {count} tries!")
