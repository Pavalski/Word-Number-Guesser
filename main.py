import random
import os 
import time
from termcolor import colored 
from words import words
from valid_words import valid_words

def make_code():
  """ Creates the code for the game """  
  global code, code_count
  
  code = []
  code_count = []
  
  if n_w == "n":
    for _ in range(5):
      num = random.randint(0, 9)
      if dup == "y":
        code.append(num)
      else:  
        while True:
          if not num in code:
            code.append(num)
            break
          num = random.randint(0,9)
          
  elif n_w == "w":
    code = random.choice(words)
    for letter in code:
      code_count.append(letter)

def guess_num_code():
  """ Lets the player guess the number code. 
  Also, it checks if any of the numbers are in the code and if it's in the right spot.
  Checks if the player guessed the code. 
  """
  global game_over, correct, guess, win
  
  amnt = [] # Values that are in the code but are in the wrong spot
  correct = []
  win = 0
  
  while True:
    try:
      vle = 0
      guess = []
      guess_str = input("Guess code: ")
      for num in guess_str:
        guess.append(int(num))
      
      if len(guess) != 5:
        print("5 numbers please.")
        
      else:
        for value in guess:
          if vle == 0:
            if value < 0 or value > 9:
              print("0 - 9 please")
              time.sleep(1)
              vle = 1
        if dup == "n":      
          dup_guess = set(guess)
          if len(dup_guess) != len(guess):
            print("No duplicates")  
            time.sleep(1)
            vle = 1
          
        if vle == 0:
          for pos, num in enumerate(guess):
            if code[pos] == num:
              correct.append(num)
            else:
              correct.append("_")
          for pos, num in enumerate(guess):
            if num in code and code[pos] != num:
              if code.count(num) != (correct.count(num) + amnt.count(num)):
                amnt.append(num)
              else:
                amnt.append("_")
            else:
              amnt.append("_")
              
          amnt_sv.append(amnt)
          correct_sv.append(correct)
          guess_rows.append(guess)
          if guess == code:
            game_over = True
            win = 1
          print("\n\n")
          break
      time.sleep(2)
      os.system("cls")
      show_board()
      
    except ValueError:
      print("No spaces and just numbers please.")
      time.sleep(2)
      os.system("cls")
      show_board()

def guess_word_code():
  """ Lets the player guess the word code. 
  Also, it checks if any of the letters are in the code and if it's in the right spot.
  Checks if the player guessed the code. 
  """
  global game_over, correct, guess, win
  amnt = [] # Values that are in the code but are in the wrong spot
  correct = []
  win = 0
  
  while True:
    vle = 0 
    try:

      guess = input("Guess code: ")
      
      if len(guess) != 5:
        print("5-letter word please.")

      elif not guess in valid_words and not guess in words:
        print("Please use an actual word.")
      
      else:
        for value in guess:
          if vle == 0:
            if not value.isalpha():
              print("Only letters please")
              vle = 1
              
        if vle == 0:
          for pos, letter in enumerate(guess):
            if code[pos] == letter:
              correct.append(letter)
            else:
              correct.append("_")
          for pos, letter in enumerate(guess):
            if letter in code and code[pos] != letter:
              if code_count.count(letter) != (correct.count(letter) + amnt.count(letter)):
                amnt.append(letter)
              else:
                amnt.append("_")
            else:
              amnt.append("_")
              
          amnt_sv.append(amnt)
          correct_sv.append(correct)
          guess_rows.append(guess)
          if guess == code:
            game_over = True
            win = 1
          print("\n\n")
          break
      time.sleep(2)
      os.system("cls")
      show_board()
          
    except ValueError:
      print("5 numbers please.")
      time.sleep(2)
      os.system("cls")
      show_board()

def show_board():
  """ Creates and shows the board. """
  board = []
  gsnum = 0
  vlnum = 0
  letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "\n", "a", "s", "d", "f", "g", "h", "j", "k", "l", "\n", " ", "z", "x", "c", "v", "b", "n", "m"]
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  correct_place = []
  wrong_place = []
  wrong = []
  
  if turn < turn_1:
    for guesses in guess_rows:
      for value in guesses:
        if value in correct_sv[gsnum] and value == correct_sv[gsnum][vlnum]:
          print(colored(value, "green"), end = " ")
          correct_place.append(value)
        elif value in amnt_sv[gsnum] and value == amnt_sv[gsnum][vlnum]:
          print(colored(value, "yellow"), end = " ")
          wrong_place.append(value)
        else:
          print(colored(value, "red"), end = " ")
          wrong.append(value)
        vlnum += 1
      print("")
      gsnum += 1
      vlnum = 0
      
  for row in range(turn):
    board.append(["#"] * 5)
    
  for rows in board:
    print(*rows, sep = " ")
    
  print("\n")
  print(*k_code, sep = " ")
  print("\n")
  print("___________________\n") #Separates guesses and code from the avalable numbers/letters
  
  if n_w == "w":
    options = letters
  elif n_w == "n":
    options = numbers
  
  for option in options:
    if option in correct_place:
      print(colored(option, "green"), end = " ")
    elif option in wrong_place:
      print(colored(option, "yellow"), end = " ")
    elif option in wrong:
      print(colored(option, "red"), end = " ")
    else:
      print(option, end = " ")
  print("\n___________________") #Separates the available numbers/letters from the players guess
  print("\n\n")
      
def known_code():
  """ Creates a placeholder for the code on the board. 
  If the code is guessed or the player loses it shows the full code. 
  """
  global k_code
  
  k_code = ["*" for _ in range(5)]
  if turn == 0 or game_over == True:
    k_code = code

def turn_amount():
  """ Asks the player how much guesses are allowed. """
  global turn, turn_1
  
  while True:
    try:
      turn = int(input("Hows many guesses allowed?(1-10) "))
      if turn > 0 and turn <= 10:
        os.system("cls")
        break
        
      else:
        print("Between 1 and 10")
        
    except ValueError:
      print("1 value please")
      
  turn_1 = turn

def Mastermind():
  """ Runs the whole game. """
  global turn, guess_num, game_over, guess_rows, amnt_sv, correct_sv
  game_over = False
  
  instructions() 
    
  turn_amount()
  guess_num = 0
  guess_rows = []
  amnt_sv = []
  correct_sv = []
  make_code()
  
  while game_over == False and turn > 0:
    known_code()
    show_board()
    
    if n_w == "n":
      guess_num_code()
    elif n_w == "w":
      guess_word_code()
      
    turn -= 1
    os.system("cls")
    
  known_code()
  show_board()
  
  if win == 0:
    print("You lose!")
  else:
    print("You win!")
  time.sleep(4)
  os.system("cls")
  play_again()

def play_again():
  """ Asks the player if they want to play again. """
  global first_time
  
  again = input("Do you want to play again?(y/n) ").lower()
  
  if again == "yes" or again == "y": 
    first_time = False
    os.system("cls") 
    Mastermind()
  elif again == "no" or again == "n":
    print("Thanks for playing!")
  else:
    print("Please print yes or no.")
    play_again()

def instructions():
  """ States the instructions of the game. """
  if first_time == True:
    print("Welcome to Mastermind!")
    time.sleep(1)
    os.system("cls")

    print("In this game you have to guess either:\n A 5-digit number code containing numbers from 0-9\n A 5-letter word code.")
    time.sleep(4)
    os.system("cls")

  num_or_words()

  if n_w == "n":
    print(" You have to guess a 5-digit code containing the numbers 0-9 ")
  elif n_w == "w":
    print("You have to guess a 5-letter word")
  
  print(f"""
  {colored("Value", "green")}: The value is in the code and in the right spot.
  {colored("Value", "yellow")}: The value is in the code but in the wrong spot. 
  {colored("Value", "red")}: The number is not in the code.\n""")
  
  while True:
    cont = input("Are you ready to start?(y/n) ").lower()
    if cont == "y" or cont == "yes":
      os.system("cls")
      break

def num_or_words():
  """ Asks the player if they want the code to be numbers or a word """
  global n_w, dup

  while True:
    n_w = input("Do you want the code to be numbers(n) or words(w)? ").lower()

    if n_w == "n":
      os.system("cls")
      
      while True:
        dup = input("Are duplicates allowed?(y/n) ").lower()
        if dup == "y" or dup == "n":
          os.system("cls")
          break
          
      break
    elif n_w == "w":
      os.system("cls")
      break

first_time = True

Mastermind() # Starts the game