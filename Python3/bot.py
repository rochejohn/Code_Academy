def cs_service_bot():
    # Replace `pass` with your code
    print('Hello! Welcome to the DNS Cable Company\'s Service Portal. Are you a new or existing customer?\n[1] New Customer\n[2] Existing Customer')
    response = input('Please enter the number corresponding to your choice:')
    if response == '1':
        new_customer()
    elif response == '2':
        existing_customer()
    else:
        print('Sorry, we didn\'t understand your selection.')
        cs_service_bot()


def existing_customer():
    # Replace `pass` with your code
    
    ans = input('What kind of support do you need?\n[1] Television Support\n[2] Internet Support\n[3] Speak to a support representative.')
    if ans == '1':
        television_support()
    
    if ans == '2':
        internet_support()
        
    if ans == '3':
        live_rep('support')
        
    else:
        print('Sorry, we didn\'t understand your selection.')
        existing_customer()
        
def new_customer():
    # Replace `pass` with your code
    
    ans = input('What kind of support do you need?\n[1] Sign up for service.\n[2] Schedule a home visit.\n[3] Speak to a sales representative.')
    if ans == '1':
        sign_up()
    
    elif ans == '2':
        home_visit()
        
    elif ans == '3':
        live_rep('sales')
        
    else:
        print('Sorry, we didn\'t understand your selection.')
        new_customer()


def television_support():
    # Replace `pass` with your code
    ans = input('What is the nature of your problem?\n[1] I can\'t access certain channels.\n[2] My picture is blurry.\n[3] I keep losing service.\n[4] Other issues.')
    
    if ans == '1':
        print ('Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.')
        did_that_help()
        
    elif ans == '2':
        print('Try adjusting the antenna above your television set.')
        did_that_help()
        
    elif ans == '3':
        print('Is it raining outside? If so, wait until it is not raining and then try again.')
        did_that_help()
        
    elif ans == '4':
        live_rep("support")
        
    else:
        print('Invalid option')
        television_support()
        

def internet_support():
    # Replace `pass` with your code
    ans = input('What is the nature of your problem?\n[1] I can\'t connect to the internet.\n[2] My connection is very slow.\n[3] I can\'t access certain sites.')
    
    if ans == '1':
        print ('Unplug your router, then plug it back in, then give it a good whack, like the Fonz.')
        did_that_help()
        
    elif ans == '2':
        print('Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.')
        did_that_help()
        
    elif ans == '3':
        print('Move to a different region or install a VPN. Some areas block certain sites.')
        did_that_help()
        
    elif ans == '4':
        live_rep("support")
        
    else:
        print('Invalid option')
        internet_support()
        




def did_that_help():
    # Replace `pass` with your code
    ans = input('Did the solution solve your problem?\nYes or No: ')
    ans = ans.upper()
    if ans == 'YES':
        print('Thank you')
    elif ans == 'NO':
        ans2 = input('Okay, would you rather talk to a live representative or schedule a home visit\nSelect 1 for Live Representitive.\nSelect 2 for Home Visit\nSelection: ')
        if ans2 == '1':
            live_rep('support')
        if ans2 == '2':
            home_visit('support')
        else:
            print('Invalid option! Starting again!')
            did_that_help()
    else:
        print('Invalid option! Starting again!')
        did_that_help()
        
            

def sign_up():
    # Replace `pass` with your code
    ans = input('Great choice, friend! We\'re excited to have you join the DNS family! Please select the package you are interested in signing up for.\n[1] Bundle Deal (Internet + Cable)\n[2] Internet\n[3] Cable')
    
    if ans == '1':
        print('You\'ve selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.')
        home_visit("new install")
        
    elif ans =='2':
        print('You\'ve selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.')
        home_visit("new install")
        
    elif ans == '3':
        print('You\'ve selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.')
        home_visit("new install")
        
    else:
        print('Invalid Option, Starting again!')
        sign_up()




def home_visit(purpose = 'none'):
    # Replace `pass` with your code
    if purpose == 'none':
        ans = input('What the purpose of the home visit?\n[1] New service installation.\n[2] Exisitng service repair.\n[3] Location scouting for unserviced region.')
        if ans == '1':
            home_visit("new install")
        elif ans == '2':
            home_visit("support")
        elif ans == '3':
            home_visit("scout")
        else:
            print('Invalid Input, restarting')
            home_visit()
            
    else:
        visit_date=input('Please enter a date below when you are available for a technician to come to your home and assist with %s.' %purpose)
        print(' Wonderful! A technical will come visit you on %s. Please be available between the hours of 1:00 am and 11:00 pm.' %visit_date)
        return visit_date


def live_rep(purpose):
    # Replace `pass` with your code
    if purpose == 'sales':
        print('Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.')
    if purpose == 'support':
        print('Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.')


cs_service_bot()