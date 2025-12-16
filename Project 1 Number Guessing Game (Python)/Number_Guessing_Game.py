import random

secrate_number = random.randint(1,100)

attempts = 0
print("** Welcome To Number Guessing Game **")
print("Guess The Number Between (1 TO 100) ")



while True:
    guess = int(input("Enter a Number Between 1 to 100:- "))
    attempts = attempts + 1

    if guess > secrate_number:
        print("The Guess Is Too High")

    elif guess < secrate_number:
        print("The Guess is Too Low")
    
    else:
        print(f"This {guess} Guessed Number is Correct ")
        print("Total Attempts", attempts)
        break