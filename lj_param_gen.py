import numpy as np 
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file',help='enter txt file')
args = parser.parse_args()

# read .xyz file

input_file = open(args.input_file, 'r')
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

#define functions

# 9-6 mixing rule 
def espsilon_ljtype9(e1, s1, e2, s2) -> float:
    return (2*np.sqrt(e1*e2)*(s1**3)*(s2**3))/((s1**6)+(s2**6))
    
def sigma_ljtype9(s1, s2) -> float:
    return (((s1**6 + s2**6)/2))**(1/6)
    
# 12-6 mixing rule
def espsilon_ljtype12(e1, e2) -> float:
    return np.sqrt(epsilon[i]*epsilon[j])
    
def sigma_ljtype12(s1, s2) -> float :
    return (sigma[i] + sigma[j])/2

#initialize parameter matrix
sigmas_out = np.matrix([[0]*index[-1]]*index[-1], dtype=np.float64)
epsilons_out = np.matrix([[0]*index[-1]]*index[-1], dtype=np.float64)

#generate combination rules

for i in range(len(index)):
    for j in range(len(index)):
        #compute pure 9-6 lj parameters
        if (lj_type[i] == '9') and (lj_type[j] == '9'):
            epsilons_out[[i],[j]] = espsilon_ljtype9(epsilon[i], epsilon[j], sigma[i], sigma[j]) 
            sigmas_out[[i],[j]] = sigma_ljtype9(sigma[i], sigma[j])
        #compute mixed parameters 
        elif (lj_type[i] == '12') and (lj_type[j] == '9'):
            sigma[i] = sigma[i]*(2**(1/6))
            epsilons_out[[i],[j]] = espsilon_ljtype9(epsilon[i], epsilon[j], sigma[i], sigma[j]) 
            sigmas_out[[i],[j]] = sigma_ljtype9(sigma[i], sigma[j])
        #compute pure 12-6 parameters
        else:
            epsilons_out[[i],[j]] = espsilon_ljtype12(epsilon[i], epsilon[j]) 
            sigmas_out[[i],[j]] = sigma_ljtype12(sigma[i], sigma[j])

with open('lj_parameters.out', 'w') as f:
    for i in range(len(index)):
        for j in range(len(index)):
            if j >= i:
                if (lj_type[i] == '9') and (lj_type[j] == '9'):
                    print('pair_coeff  ', i + 1, j + 1, ' lj/class2/coul/long  ',
                           "%.7f" % float(epsilons_out[[i],[j]]), "%.7f" % float(sigmas_out[[i],[j]]), file=f)
                elif (lj_type[i] == '12') and (lj_type[j] == '9'):
                    print('pair_coeff  ', i + 1, j + 1, ' lj/class2/coul/long  ',
                           "%.7f" % float(epsilons_out[[i],[j]]), "%.7f" % float(sigmas_out[[i],[j]]), file=f)
                else:
                    print('pair_coeff  ', i + 1, j + 1, ' lj/cut/coul/long     ', 
                          "%.7f" % float(epsilons_out[[i],[j]]),  "%.7f" % float(sigmas_out[[i],[j]]), file=f)
