import random
option = ("rock", "paper", "scissors")
running = True
while running:
   player = None
   computer = random.choice(option)

   while player not in option:
           player = input("enter a choice (Rock, Paper, Scissors): ")
   print(f"palyer:{player}")
   print(f"computer:{computer}")
   if computer == player:
       print("it's a tie")
   elif player == "rock" and computer == "scissors":
       print("you win!")
   elif player == "paper" and computer == "rock":
       print("you lose!")
   elif player == "scissors" and computer == "paper":
       print("you win!")
   elif player == "paper" and computer == "scissors":
       print("you lose!")
   elif player == "scissors" and computer == "rock":
       print("you lose!")
   elif player == "rock" and computer == "paper":
       print("you win!")
   if not input("play again (y/n): ").lower() == "y":
       running = False
print("thank you for playing")
