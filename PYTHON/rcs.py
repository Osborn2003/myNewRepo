import random

def get_choices():
      options = ("rock", "paper", "scissors")
      player_choice = input("Enter Choice (rock, paper, scissors): ").lower()
      computer_choice = random.choice(options)
      choices = {
        "player": player_choice, "computer":computer_choice
      }
      return choices


def validate_winner(player, computer):
      print(f"You choose {player}, computer choose {computer}.")
      if player == computer:
          return "It's a tie."
      elif player == "rock":
          if computer == "scissors":
              return "Rock smashes scissors. You Win!"
          else :
              return "Paper covers rock. You Lose."
      elif player == "paper":
          if computer == "rock":
              return "Paper covers rock. You Win!"
          else :
              return "Scissors cuts paper. You Lose."
      elif player == "scissors":
          if computer == "paper":
              return "Scissors cuts paper. You Win!"
          else :
              return "Rock smashes scissors. You Lose."

choices = get_choices()
result = validate_winner(choices["player"], choices["computer"])
print(result)