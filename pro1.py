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
