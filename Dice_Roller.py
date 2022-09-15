import random

def roll_dice():

    dice_drawing = {
        1: (
            "┌─────────┐",
            "│    1    │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│    2    │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ● 3    │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    4    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ● 5 ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ● 6 ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),

    }    

    while True:

        roll = input("Roll the dice? (Yes/No): ")

        if roll.lower() == "Yes".lower():
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)

            print("Dice Rolled: {} and {}".format(dice1, dice2))
            print("\n".join(dice_drawing[dice1]))
            print("\n".join(dice_drawing[dice2]))
        
        elif roll.lower() == "No".lower():
            print("Ending Program...")
            break
            
        else:
            print("Please input \"Yes\" or \"No\" \n")

roll_dice()