import numpy as np 
import pandas as pd

input_file = open('parameters_file.txt','r')
lines = input_file.readlines()

index = []
lj_type = []
epsilon = []
sigma = []

for i in lines:
    line = i.split()
    index.append(int(line[0]))
    lj_type.append(line[1])
    epsilon.append(float(line[2]))
    sigma.append(float(line[3]))

print(len(index))
print(lj_type)
for i in range(len(index)):
    for j in range(len(index)):
        if (lj_type[i] == '12') and (lj_type[j] == '12'):
            print('same lorentz-berthelot rule')
        else: 
            print('different lj type')
