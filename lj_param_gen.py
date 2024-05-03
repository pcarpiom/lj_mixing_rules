import numpy as np 
import pandas as pd

input_file = open('parameters_file.txt','r')
lines = input_file.readlines()

for l in lines:
    print(l.split())
