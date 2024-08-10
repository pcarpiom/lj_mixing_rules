# lj_mixing_rules
This script creates combining rules from a set of 12-6/9-6 epsilon/sigma parameters. The input file is a .txt file with the following structure. 

Index LJ-type* Epsilon Sigma 

*LJ-type refers to the Lennard-Jones potential type. Two types are implemented 
 
 ## 12 for Lorentz-Berthelot rules (12-6 parameters)

  $\displaystyle \epsilon _{ij}={\sqrt {\epsilon _{ii}\epsilon _{jj}}}$, $\displaystyle \sigma _{ij}={\frac {\sigma _{ii}+\sigma _{jj}}{2}}$

 ## 9 for Waldman-Hagler rules (9-6 parameters)

  $\displaystyle \epsilon_{ij}=2{\sqrt {\epsilon_{i}\cdot \epsilon{j}}}\left({\frac {(r_{i}^{0})^{3}\cdot (r_{j}^{0})^{3}}{(r_{i}^{0})^{6}+(r_{j}^{0})^{6}}}\right)$, $\displaystyle r_{ij}^{0}=\left({\frac {(r_{i}^{0})^{6}+(r_{j}^{0})^{6}}{2}}\right)^{1/6}$

 
Waldman-Hagler rules are generated for the case of mixed interactions. 

