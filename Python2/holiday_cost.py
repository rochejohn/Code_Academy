def hotel_cost(nights):
  return nights * 140

def plane_ride_cost(city):
  city = city.lower()
  if city == 'charlotte':
    return 183
  elif city == 'tampa':
    return 220
  elif city == 'pittsburgh':
    return 222
  elif city == 'los angeles':
    return 475
  
def rental_car_cost(days):
  cost = 40
  total = days * cost
  if days >= 7:
    total -= 50
    return total
  elif days >= 3:
    total -= 20
    return total
  else:
    return total
  
def trip_cost(city,days, spending_money):
  total = rental_car_cost(days) + hotel_cost(days-1) + plane_ride_cost(city) + spending_money
  return total
  
#print trip_cost('los angeles',5, 600)

print 'To calculate price of trip please enter the following: '
print 'Destination: Charlotte, Tampa, pittsburgh, or Los Ageles'
city = raw_input('Destination: ')

print 'How many days: '
days = int(raw_input('Days: '))

print "How much spending money: "
spending_money = int(raw_input('Money: '))

total = trip_cost(city,days, spending_money)

print "Your trip to %s for %s days's with an additional %s spending money will cost you a total of %s euros!!" % (city, days, spending_money, total)