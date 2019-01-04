'''cheapest shipping by weight using drone ship or premium ship'''




def ground(weight):
  flatfee=20
  if weight <= 2:
    cost = (weight * 1.5)

  elif weight > 2 and weight <=6:
    cost = (weight * 3)

  elif  6< weight <=10:
    cost = (weight * 4)
  
  elif weight >10:
    cost = (weight * 4.75)
  
  return cost + flatfee
 
  
prem_ground = 125

def drone(weight):
  
  if weight <= 2:
    cost = (weight * 4.5)

  elif weight > 2 and weight <=6:
    cost = (weight * 9)

  elif  6< weight <=10:
    cost = (weight * 12)
  
  elif weight >10:
    cost = (weight * 14.25)
  
  return cost

def cheap(weight):
  gc =ground(weight)
  dc = drone(weight)
  pgc = prem_ground
  
  if gc < dc and gc < pgc:
    print('Ground Shipping is the cheapest method for the weight %s and it will cost %s' %(weight,gc))
  
  elif dc < gc and dc < pgc:
          print('Drone Shipping is the cheapest method for the weight %s and it will cost %s' %(weight,dc))
  
  else:
                print('Premium Ground Shipping is the cheapest method for the weight %s and it will cost %s' %(weight,pgc))
          
        
cheap(1.5)