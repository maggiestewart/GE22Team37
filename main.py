# Geaux Engineering 2022
# Team 37
# Project Choice: Compile your adventure
# Project Name: Unexpected Landing

import designProjectFunction

# number of pieces = 0 at the start
playerInventory = 0

print("OH NO! While on your LSU space exploration you crashed on Planet PFT 1269 and lost 3 important pieces of your spaceship. You must now leave the ship so you can continue exploring.\n")

#user input
choice = input("Where do you go first to find the pieces, a CRATER or the OCEAN?\n")

# if user selects CRATER
if choice == "CRATER":
    designProjectFunction.crater(playerInventory) 
    designProjectFunction.ocean(playerInventory)
    designProjectFunction.finalBattle(playerInventory)

# if user selects OCEAN
elif choice == "OCEAN":
    designProjectFunction.ocean(playerInventory)
    designProjectFunction.crater(playerInventory)
    designProjectFunction.finalBattle(playerInventory)   
  