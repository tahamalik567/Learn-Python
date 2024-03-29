print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
                                                             
      ''')
print("Welcome to Treasure Island.  Your mission is to find the treasure.")
choice=input("you want to go 'left' or 'right'?").lower()
if choice  != "left":
    print("Fall into a hole. Game Over")
else:
    choice=input("you want to 'swim' or 'wait'?").lower()
    if choice != "wait":
        print("Attacked by trout. Game Over")
    else:
        choice=input("which door? choose 'Red', 'Blue' or 'Yellow'?").lower()
        if choice == "red":
            print("Burned by fire. Game Over")
        elif choice == "blue":
            print("Eaten by beasts. Game Over")
        elif choice == "yellow":
            print("You Win!")
        else:
            print("Game Over")

    