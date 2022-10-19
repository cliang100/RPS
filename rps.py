import random

score = 0
while score < 5:
    user_action = input("Beat Robert at rock paper scissors 5 times to win: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, Robert chose {computer_action}\n")

    if user_action == computer_action:
        print(f"Uh oh spaghettio it's a tie since you both chose {user_action}\nTry again!") 
    elif user_action == "rock":
        if computer_action == "scissors":
            score = score + 1
            print(f"You won!\nScore: {score}")
        else:
            print("Better luck next time...")
            break
    elif user_action == "paper":
        if computer_action == "rock":
            score = score + 1
            print(f"You won!\nScore: {score}") 
        else:
            print("Better luck next time...")
            break
    elif user_action == "scissors":
        if computer_action == "paper":
            score = score + 1
            print(f"You won!\nScore: {score}")    
        else:
            print("Better luck next time...")
            break

#The greatest rock paper scissors simulator. Ever.