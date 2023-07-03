import random
def generate_choice():
  return random.choice(['rock', 'paper', 'scissors'])
def compare_choices(choice1, choice2):
  """Compares two choices of 'rock', 'paper', or 'scissors' and determines the winner."""
  if choice1 == choice2:
    return 'tie'
  elif choice1 == 'rock' and choice2 == 'scissors':
    return 'rock'
  elif choice1 == 'paper' and choice2 == 'rock':
    return 'paper'
  elif choice1 == 'scissors' and choice2 == 'paper':
    return 'scissors'
def play_game():
  """Plays the game of rock paper scissors."""
  player_choice = input('Choose your choice: rock, paper, or scissors? ')
  computer_choice = generate_choice()
  print('The computer chose {}.'.format(computer_choice))
  if compare_choices(player_choice, computer_choice) == 'tie':
    print('The game is a tie.')
  elif compare_choices(player_choice, computer_choice) == player_choice:
    print('You win!')
  else:
    print('You lose!')
def main():
  """Runs the game of rock paper scissors."""
  play_game()
if __name__== '__main__':
  main()