# This is a game about guessing a randomly generated number
import random

def again():
    print('Guess again.')

def debug(): # This string allows for debugging by revealing the secret number to test accurate funcitonality
    print('DEBUG: The secret number is ' + str(secretNumber))

secretNumber = random.randint(1, 20)

print('Hello, what is your name?')
name = input()

if name == 'admin': # Cheat code
    debug()

print('Well, ' + name + ', I am thinking of a number between 1 and 20. Take a guess.')

# Ask the player to guess 6 times

for guessesTaken in range(1, 7):

    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Well done, ' + name + ' you guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber) + '. Better luck next time!')
