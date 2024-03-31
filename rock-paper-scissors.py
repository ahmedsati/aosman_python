import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

playAgain = True

while playAgain != False:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!") 
      
    else:
        print(game_images[user_choice])
      
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])
      
        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        
        
        elif computer_choice > user_choice:
            print("You lose")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice == user_choice:
            print("It's a draw")
    
    user_input = input("Would you like to play again? Type y for Yes or n for No\n")
    if user_input == 'y':
        playAgain = True
    elif user_input == 'n':
       playAgain = False
       print("Thank you for playing!")
    else:
        print(input("You have typed the wrong input, please type y for Yes or n for No\n"))