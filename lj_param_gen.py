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