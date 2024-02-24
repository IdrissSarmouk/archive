#replit's Build A Simple Python Game 
import random
#SWBAT identify which built-in functions to be used for creating a secret number
#The computer will pick one secrect number and a player has to guess the secret number.
number = random.randint(1, 100)
#Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
# Players have to guess the correct number within 7 attempts
#SWBAT combine for loop with other flow controls in Python and write a condition to properly teminate the for loop
for i in range(1, 8):
    guess = int(input("Guess the number: "))

    if guess == number: 
        print(f"Great! You guessed the secret number {i} guesses.") #In case the player successfuly guessed the secret number within 7 attempts, the program will say, "Great! You guessed the secret number in N guesses." For example, if the correct guess was at 5th attempt, the following message should appear. "Great! You guessed the secret number in 5 guesses."
        break
    elif guess < number:
        print("Your number is too low.")
    else: #If the guess is higher than the secret number, the program will say, "Your number is too high.". If the guessed number is lower, then the progam will say, "Your number is too low."
        print("Your number is too high.")
else:
    print(f"You failed. The secret number was {number}.")  #If the player failed to guess the secrect number within 7 attempts, the program will say, "You failed. The secret number was N .". For example, let's say the secret number was 13 then the message should be, "You failed. The secret number was 13."
