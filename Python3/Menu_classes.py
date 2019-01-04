class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time= end_time
    
  def calculate_bill(self,purchased_items):
      self.purchased_items= purchased_items
      total = 0
      for item in self.purchased_items:
        total += self.items[item]
      return total
    
  def __repr__(self):
    return('{menu} Menu!\nServed from {s}:00 to {e}:00').format(menu=self.name.title(),s=self.start_time,e=self.end_time)
    
    
brunch = Menu('brunch',{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},11,16)

early_bird = Menu('early_bird',{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

dinner = Menu('dinner',{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17,23)

kids = Menu('kids',{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11,21)

#print(brunch)

#print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
    
    
  def __repr__(self):
    
    return('{add} location!').format(add=self.address)
  
  
  def available_menus(self,time):
    avail=[]
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        avail.append(menu)
    options = ''
    for x in avail:
      options += '\n%s\n' %x
    return options
    
menus = [dinner, early_bird, kids, brunch]
    
flagship_store = Franchise('1232 West End Road',menus)

new_instalment = Franchise('12 East Mulberry Street',menus)


fran = [flagship_store, new_instalment]

class Business:
  def __init__(self,name,fran):
    self.name= name
    self.fran = fran
    
  def __repr__(self):
    return('This is the {bus} business, it consists of the following franchises: {fran}'.format(bus=self.name,fran=self.fran))

  
  
basta_old = Business('Basta Fazoolin\' with my Heart', fran)

arepas_menu = Menu('Take a\' Arepa',{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
},10,20)

arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

basta_new = Business('Take a\' Arepa',arepas_place)
 
#print specific menu and available time  
print(brunch) 

#shows specifici menu and prices
print(brunch.items) 

  
#shows available menu at specific time you book for 
print(flagship_store.available_menus(17))

#shows the business names and franchises
print(basta_old)
print()
print(basta_new)

#shows specific menus

#calculates bill
brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])