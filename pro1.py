import numpy as np
import math
import random

pattern = []
classes = []

filename = 'iris99.csv'
file = open(filename,'r')
#fopen=('iris99.csv','r')

for line in file.readlines():
    row = line.strip().split(',')
    pattern.append(row[0:4])
    classes.append(row[4])
print("Iris Data Loaded")
file.close

pattern = np.array(pattern)

sample_no = np.random.randint(0,len(pattern))

print("Sample pattern: " + str(pattern[int(sample_no)]))
print("Class of the above pattern: " + str(classes[int(sample_no)]))

##for calculating no. of maps unit

def mapunits(ip_len,size='small'):
    
    hmap_units = 5*ip_len**0.54321
     
    if size == 'big':
        hmap_units = 4*(hmap_units)
    else:
        hmap_units = 0.25*(hmap_units)
        
    return hmap_units
        
        
map_units = mapunits(len(pattern),size='big')
print("Heuristically computed appropriate no. of map units: "+str(int(map_units)))

