'''This script will attempt to play rock paper scissors'''


import random, time


options = ['ROCK','PAPER','SCISSORS']

message={
  'tie':'Yawn its a tie!',
  'win': 'Yay you have won!',
  'lost': 'Aww you lost!'
}
def decide_winner(user_choice, computer_choice):
  print 'You have chosen %s !!' % user_choice
  print 'Computer is thinking.....'
  time.sleep(2)
  print 'Computer has chosen %s !!' % computer_choice
  
  if user_choice == computer_choice:
    print message['tie']
    
  elif user_choice == options[0] and computer_choice == options[2]:
    print message['win']
  
  elif user_choice == options[1] and computer_choice == options[0]:
    print message['win']
    
  elif user_choice == options[2] and computer_choice == options[1]:
    print message['win']
    
  else:
    print message['lost']
  
def play_RPS():
  print 'Hello, please enter your choice of Rock, Paper or Scissors: '
  user_choice = raw_input()
  user_choice = user_choice.upper()
  computer_choice = options[random.randint(0,2)]
  decide_winner(user_choice,computer_choice)
  print 'Would you like to play again? (y/n)'
  ans = raw_input()
  ans = ans.lower()
  if ans == 'y':
    play_RPS()
  else:
    print 'Goodbye for now!!'
  
play_RPS()
  