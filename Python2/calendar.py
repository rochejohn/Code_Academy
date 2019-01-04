'''create a command line calendar'''

from time import strftime,sleep,gmtime

name = 'John'

calendar = {}

def welcome():
  print 'Hello %s, welcome to your calendar' % name
  print "Calander is now opening!"
  sleep(1)
  print strftime ('%A %B %d, %Y')
  print strftime ('%H:%M:%S')
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start == True:
    user_choice= raw_input('Please enter:\n A to Add\n U to Update\n V to View\n D to Delete\n X to Exit:\nChoice: ')
    user_choice = user_choice.upper()
    if user_choice=='V':
      if len(calendar) < 1:
        print 'Your Calendar is empty!'
      else:
        print calendar
    
    elif user_choice == 'U':
      date = raw_input('What date?: ')
      update = raw_input('Whats the update?: ')
      calendar[date]=update
      print 'Update is successful!'
      print calendar
     
    elif user_choice == 'A':
      event = raw_input('Enter event: ')
      date = raw_input('Enter date (MM/DD/YYYY): ')
      if len(date) > 10 or date[6:10] < int(strftime ('%Y')):
        print 'You have entered an invalid date format.'
        try_again = raw_input('Try Again? Y for Yes, N for No: ')
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
          
      else:
          calendar[date]= event
          print 'The event is successfully added.'
          print calendar
          
    elif user_choice == 'D':
      if len(calendar.keys) < 1:
        print "The Calender is empty!"
      else:
        event = raw_input('What event: ')
        
        
        for date in calendar.keys:
          if calendar[date] == event:
            del calendar[date]
            print 'Event Deleted!'
            print calendar
            
        else:
            print 'Incorrect Event Specified!'
            
    elif user_choice == 'X':
      print 'The program is not exiting!! Goodbye'
      sleep(2)
      start == False
      
    else:
      print 'Invalid Error, exiting!'
      start == False
      
start_calendar