"""import random

# randrange does not print the start and stop numbers
Random = random.randrange(-1 , 10)
print(Random)

# Prints a random number between 0 to the range-1
Random = random.randrange(10)
print(Random)

# randint prints the start and stop numbers, and it must have a start and stop range
Random = random.randint(-1 , 10)
print(Random)"""


import random

top_of_range = input("Please type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please typer a number greater than zero next time.")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0 , top_of_range)
guesses = 0
#while user_guess != random number:

while True:
    guesses +=1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number:
        print("You got it above the number!")
    else:
        print("You got it below the number")

print("You got it in " , guesses , " guesses!")