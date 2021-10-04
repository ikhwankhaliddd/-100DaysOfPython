#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
#ANSWER_NUMBER = random.randint(1,100) To check the Answer
print(ANSWER_NUMBER)
HARD_ATTEMPTS = 4
EASY_ATTEMPTS = 9

def main_page() : 
  print(logo)

def play_game() : 
  difficulty = input("Choose your difficulty. type 'easy' or 'hard'\nAnswer : ")
  

  if difficulty == 'easy':
    for attempt in range(EASY_ATTEMPTS,-1,-1) :
      guess_number = int(input("Make guess : "))
      if guess_number < ANSWER_NUMBER :
        print("Too low")
        print(f"You have {attempt} attempts remaining to guess the number.")
        if attempt == 0 :
          print("You've ran out of attempts, You lose")

      elif guess_number > ANSWER_NUMBER :
        print("Too High")
        print(f"You have {attempt} attempts remaining to guess the number.")
        if attempt == 0 :
          print("You've ran out of attempts, You lose")

      elif guess_number == ANSWER_NUMBER :
        print("Correct!")
        break;

  if difficulty == 'hard':
    for attempt in range(HARD_ATTEMPTS,-1,-1) :
      guess_number = int(input("Make guess : "))
      if guess_number < ANSWER_NUMBER :
        print("Too low")
        print(f"You have {attempt} attempts remaining to guess the number.")
        if attempt == 0 :
          print("You've ran out of attempts, You lose")

      elif guess_number > ANSWER_NUMBER :
        print("Too High")
        print(f"You have {attempt} attempts remaining to guess the number.")
        if attempt == 0 :
          print("You've ran out of attempts, You lose")

      elif guess_number == ANSWER_NUMBER :
        print("Correct!")
        break;


main_page()
play_game()




