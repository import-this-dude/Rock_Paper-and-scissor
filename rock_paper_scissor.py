# ROCK PAPER SCISSORS GAME
'''
HERE ROCK=1
PAPER =2
SCISSORS=3
'''

import random
while True:
    your_choice = input("Enter your choice : ").lower()
    choice = { "r" : 1 , "p" : 2 , "s" : 3}
    if your_choice not in choice:
        print("Invalid Input")
        continue
    else:
        bot = random.choice([1, 2, 3])
        main_choice = ({1 : "Rock" , 2 : "Paper" , 3 : "Scissors" })
        you = choice[your_choice]
        print(f"Your choice {main_choice[you]} \n Bot choice {main_choice[bot]}")

        if( bot == you ):
            print(" Its Draw !!!")
        else:
            if(bot == 1 and you ==2):
                print(" You Won !!")
            elif(bot == 1 and you == 3):
                print("Bot won you lost")
            elif(bot == 2 and you == 1):
                print("Bot won You Lost !!!")
            elif(bot == 2 and you == 3):
                print("You won !!")
            elif(bot == 3 and you == 1):
                print(" You Won !!!")
            elif(bot == 3 and you == 2):
                print("Bot won , YOu Lost!!!")
    again= input("\nPlay again? (y/n): ").lower()
    if again == "n":
        print("Thanks for playing! 👋")
        break   
    

