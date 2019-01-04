'''This script will roll dice twice, user has to guess correct or Pc wins'''

import random, time

def get_user_guess():
  print 'Please guess what you think the 2 dice rolls adds up to: '
  guess = int(raw_input('Guess: '))
  return guess


def roll_dice(number_of_sides):
  first_roll = random.randint(1,number_of_sides)
  sec_roll = random.randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print 'The max value rolled is %d' % max_val
  #guess = get_user_guess()
  guess = get_user_guess()

  if guess > max_val:
    print 'This guess is too high'
  
  else:
    print 'Rolling.....'
    time.sleep(2)
    print 'The first roll is %d' % first_roll
    time.sleep(1)
    print 'The second roll is %d' % sec_roll
    time.sleep(1)
    total_roll = first_roll + sec_roll
    print 'The total roll is %d' % total_roll
    print 'Result.....'
    time.sleep(1)
    if guess == total_roll:
      print 'Congrats you have won a million dollars!!'
    else:
      print 'You owe 5 thousand dollars!!!'
    

    
def gamenow():
  print 'Hello, Welcome to the dice game!'
  print 'Select the number of sides per dice:'
  sides = int(raw_input('Sides: '))
  roll_dice(sides)
  print 'Would you like to gamble again?'
  ans = raw_input('y or n: ' )
  ans = ans.lower()
  if ans == 'y':
    gamenow()
    
  else:
    print 'GoodBye!!'
  
gamenow()  