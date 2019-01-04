'''dna sample'''
sample = ['GTA','GGG','CAC']


'''takes the suspect text file and reads into dna data'''
def read_dna(dna_file):
  dna_data= ''
  with open(dna_file,'r') as f:
    for line in f:
      dna_data += line
  return dna_data
 
  '''this takes the text file read into dna data variable
  
  it then creates an empty list
  
  iterates thru list in steps on 3s (size of dna codons
  
  appends codons if at least 3 characters
  
  variable moving append 
  codons.append(dna[x:x+3]) << nice piece
  
  adds all suspects codons to lists codons
  
  )'''
def dna_codons(dna):
  codons = []
  for x in range(0,len(dna),3):
    if x + 3 < len(dna):
      codons.append(dna[x:x+3])
  return codons
      
  
  '''iterates thru codons list and checks if each one is in sample codons 
  
  counts each up'''
def match_dna(dna):
  matches = 0
  for x in dna:
    if x in sample:
      matches += 1
  return matches
  
  
  
  
'''checks if suspect has more than 3 matching codons to continue investigating otherwise frees suspect'''  

'''takes in text file'''
def is_criminal(dna_sample):
  
  '''read txt file to variable'''
  dna_data = read_dna(dna_sample)
  
  '''extracts codons from dna suspects read string and adds each to a list'''
  codons = dna_codons(dna_data)
  
  '''checks list each against samples'''
  num_matches = match_dna(codons)
  
  if num_matches > 3:
    print 'The number of matches is %d, this warrents the investigation to continue with this suspect.' %num_matches
    
  else:
    print 'The number of matches is %d, this does not warrent the investigation to continue with this suspect, suspect can be freed.' %num_matches
    
print "Suspect One"
is_criminal('suspect1.txt')

print "Suspect Two"
is_criminal('suspect2.txt')

print "Suspect Three"
is_criminal('suspect3.txt')
    
  
    