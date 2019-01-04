  '''  edit to check git diff'''

'''This will be used to calculate the area of a shape'''

print 'Area Calculator is now up and running!!'

print "Please select one of the following shapes: Circle or Triange."
option = raw_input('c or t:')
option = option.lower()

if option == 'c':
  print 'Please provide the radious of the circle in cm: '
  radius = float(raw_input('radius: '))
  area = 3.14159 * radius **2
  print 'The area of your Circle is ' + str(area)+'!!!'
  
elif option == 't':
  print 'Please provide the base of the Triangle: '
  base= float(raw_input('base in cm: '))
  print 'Please provide the height of the square: '
  height= float(raw_input('height in cm: '))
  area = base/2.0 * height
  print 'The area of your Triangle is ' + str(area)+'!!!'

else:
  print 'You did not enter c or t, try again'
  
print 'now exiting'
