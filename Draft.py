#  Variables.
import random
guess = random.randint(1, 100)  # The random number.
guessed = 0  # Number of guessed turns.
left = 9  # Turns left.


#  Basic greetings.
print("Welcome to Guess the Number!\n")
print("let's start!\n")

#  Introduction and user input.
name = str(input("What is your name?: "))
print("Dear ", name, ", please fire your brain cells.")
x = int(input("Guess a number between 1 and 100. Attention, you will have 9 tries!: "))
while True:
    print()
    if 100 >= x >= 1:
        break
    else:
        x = int(input("Guess a number between 1 and 100. Attention, you will have 9 tries!: "))
#  Function in action.
while guessed < 9:
    print()
    guessed = guessed + 1
    left = left - 1
    if x < guess:
        print("You have ", left, " tries left.")
        x = int(input("Enter a higher number: "))
    elif x > guess:
        print("You have ", left, " tries left.")
        x = int(input("Enter a lower number: "))
    elif x == guess:
        break

if x == guess:
    guessed = str(guessed)
    print("You guessed it! Bravo ", name, "! And you guessed in ", guessed, " turns!")

if x != guess:
    guess = str(guess)
    guessed = str(guessed)
    print("Tough luck ", name, ". The answer is ", guess, ". You wasted ", guessed, "turns")

print("Thank you for your participation!")

