# Geaux Engineering 2022
# Team 37
# Project Choice: Compile your adventure
# Project Name: Unexpected Landing

import random

# this is a function that brings the user to the crater option in the storyline
def crater(playerInventory):
  print("\nYou've arrived at the crater. You see the alien with one of your pieces. You must battle them in trivia to win your piece back.\n")
  # loops 3 times or less, giving the user 3 tries
  for x in range(3):
    answer = input("The aliens give you three tries to answer the following question correctly: \n When were the indian mounds created? A. More than 5000 years ago, B. 2020, C. 1727\n")
    if answer == "A":
      print("Congrats! You got the answer correct. The aliens reward you by returning your missing piece.\n")
      # adds a piece / tally to the inventory
      playerInventory+=1
      break
    elif answer == "B":
      print("Your answer was incorrect, please try again.")
      print("\nAttempts left: ", 2-x)
    elif answer == "C":
      print("Your answer was incorrect, please try again.")
      print("\nAttempts left: ", 2-x)

      
# this is the function that brings the user to the ocean option in the storyline
def ocean(playerInventory):
  oceanChoice = input("\nYou've arrived at the ocean. Do you want to take a relaxing DRINK or do you want to continue your journey and SWIM through the water?\n")

  # if the user selects the drink option
  if oceanChoice == "DRINK":
    print("\nAs you drink the water, you start to feel dizzy. You pass out and discover the aliens captured you and have one of your missing pieces. You must defeat them in a game of trivia order to get your missing piece back and return to the ship.\n")
    # for loop to allow user 3 tries to answer the trivia question
    for x in range(3):
      answer = input("The aliens give you three tries to answer the following question correctly: \n What is LSU's mascot? A. Tiger, B. Lion, C. Bear\n")
      if answer == "A":
        print("\nCongrats! You got the answer correct. The aliens reward you by returning your missing piece.")
        # adds a piece to the inventory / tally
        playerInventory+=1
        break
      elif answer == "B":
        print("\nYour answer was incorrect, please try again.")
        print("\nAttempts left: ", 2-x)
      elif answer == "C":
        print("\nYour answer was incorrect, please try again.")
        print("\nAttempts left: ", 2-x)
      
  # if the user selects swim option
  elif oceanChoice == "SWIM":
    print("\nAs you are swimming, you see aliens at the bottom of the ocean with one of your missing items. They tell you that in order to get it back, you have to defeat them in a round of trivia.")
    # for loop to allow user 3 tries to answer the trivia question
    for x in range(3):
      answer = input("\nThe aliens give you three tries to answer the following question correctly: When was lsu founded? A. 1853, B. 2003, C. 1909\n")
      if answer == "A":
        print("\nCongrats! You got the answer correct. the aliens reward you for answering by returning your missing piece.")
        # adds a piece to the inventory / tally
        playerInventory+=1
        break
      elif answer == "B":
        print("\nYour answer was incorrect, please try again")
        print("\nAttempts left: ", 2-x)
      elif answer == "C":
        print("\nYour answer was incorrect, please try again")
        print("\nAttempts left: ", 2-x)

        
# this is the function that allows 
def finalBattle(playerInventory):
  print("\nWhen you arrive back at your ship, you see that the aliens have your final missing piece. They demand that you play a number guessing game in order to get it back and continue exploring.\n")

  # initializing variables for maximum guesses allowed and total guesses used
  MAX_GUESSES = 5
  guessCount = 0
  
  # selects a random integer
  mysteryNum = random.randint(0,5)

  # boolean for game result
  gameWon = False
    
  while not gameWon and guessCount<=MAX_GUESSES:
    enteredNumber = int(input("Enter a number between 0 and 5: "))
    guessCount = guessCount+1
    
    if enteredNumber == mysteryNum:
      gameWon = True
      # adds a piece to the inventory / tally
      playerInventory+=1
      print("\nYou Win!! Congrats! You have beat the final alien and retrieved the pieces. You may now proceed to the spaceship and can continue your exploration of Planet PFT 1269.")
    elif enteredNumber>mysteryNum:
      print("This number is too big.")
      print("Guess count: ", guessCount)
    elif enteredNumber<mysteryNum:
      print("This number is too small.")


  