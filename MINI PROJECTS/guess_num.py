import random
turn = 5
guess = 0
number = random.randrange(100) + 1
print("The computer is thinking of a number between 1 to 100. Try guessing it. You have 5 turns")


while guess != number and turn != 0:
    print("Turns Remaining: ", turn)
    guess = int(input("Guess a number: "))
    if guess < number and turn != 1:
        print("Guess a greater number.")
    elif guess > number and turn != 1:
        print("Guess a lower number.")
    turn -= 1
    #turn = turn - 1

if guess == number:
    print("Congratulations! You won!")
if turn == 0 and guess != number:
    print("Sorry! You ran out of turns. The computer guessed: ", number)
  
  
# Output :  
"""
The computer is thinking of a number between 1 to 100. Try guessing it. You have 5 turns
Turns Remaining:  5
Guess a number: 50
Guess a greater number.
Turns Remaining:  4
Guess a number: 80
Guess a lower number.
Turns Remaining:  3
Guess a number: 60
Turns Remaining:  2
Guess a number: 70
Guess a greater number.
Turns Remaining:  1
Guess a number: 78
Sorry! You ran out of turns. The computer guessed:  74 """