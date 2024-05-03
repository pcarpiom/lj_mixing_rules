import argparse
import numpy as np
import pandas as pd 

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='enter xyz file')
args = parser.parse_args()

#read input parameters

file = open(args.input_file, 'r')
n_params = sum(1 for line in file)
file = open(args.input_file, 'r')

print(file)