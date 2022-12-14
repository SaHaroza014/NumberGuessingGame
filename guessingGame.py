from art import logo
import random

print(logo)

numbers = list(range(1, 101))
final_num = random.choice(numbers)
print("Welcome to the Number guessing game made in Python")
print("Guess a number between 1 to 100")
difficulty = input("Choose a difficulty.Type 'easy', 'standard' or 'hard': ").lower()

def difficulty_set():
  global difficulty
  
  if difficulty == "easy":
    return 10
  elif difficulty == "standard":
    return 7
  elif difficulty == "hard":
    return 5
  else:
    flag = True
    while flag == True:
      print("Invalid input.Please try again!")
      difficulty = input("Choose a difficulty.Type 'easy', 'standard' or 'hard': ").lower()
      if difficulty == "easy" or difficulty == "standard" or difficulty == "hard":
        if difficulty == "easy":
            return 10
        elif difficulty == "standard":
            return 7
        elif difficulty == "hard":
            return 5
        flag=False

player_attempts = difficulty_set()
flag2 = True
while flag2 == True and player_attempts > 0:
    print(f'You have {player_attempts} attempts remaining to guess the number!')
    guess = int(input("Make a guess: "))
    if guess != final_num:
      player_attempts -= 1
      if guess < final_num:
        print("Guess higher!")
      elif guess > final_num:
        print("Guess lower!")
    elif guess == final_num:
      print("Correct answer!")
      flag2 = False
      
