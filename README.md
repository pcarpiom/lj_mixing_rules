# lj_mixing_rules
This script creates combining rules from a set of 12-6/9-6 epsilon/sigma parameters. The input file is a .txt with the following format: Index LJ-type* Epsilon Sigma (see example below)
```
8	12	0.0940000	3.1700000  
9	12	0.1220000	3.4700000 
10	12	0.0930000	4.1500000 
11	9	0.0680000	3.9150000 
12	9	0.0680000	3.9150000 
```
*LJ-type refers to the Lennard-Jones potential type. Two types are implemented 
 
 ## 12 for Lorentz-Berthelot rules (12-6 parameters)

  $\displaystyle \epsilon _{ij}={\sqrt {\epsilon _{i}\epsilon _{j}}}$ 
  <br />
  <br />
  $$\displaystyle\sigma _{ij}={\frac {\sigma _{i}+\sigma _{j}}{2}}$$

 ## 9 for Waldman-Hagler rules (9-6 parameters)

  $\displaystyle \epsilon_{ij}=2{\sqrt {\epsilon_{i}\cdot \epsilon_{j}}}\left({\frac {\sigma_i^{3}\cdot \sigma_j^{3}}{\sigma_i^{6}+\sigma_j^{6}}}\right)$ 
  <br />
  <br />
  $\displaystyle \sigma_{ij}=\left({\frac {\sigma_i^{6}+\sigma_j^{6}}{2}}\right)^{1/6}$

 
Waldman-Hagler rules are generated for the case of mixed interactions. 

