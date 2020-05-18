
#!/usr/local/bin/Python3

import random

# -- INPUTS/VAR -- #
n_set = ['N100', 'N200', 'N300', 'N400', 'N500', 'N600', 'N700', 'N800', 'N900', 'N1000']
gr_set = ['Gr4', 'Gr3', 'Gr2', 'Gr1', 'GrX']
slow_tyre_set = ['CM', 'SM', 'RH']
fast_tyre_set = ['CS', 'SS', 'RM', 'RS']
damage_set = ['ON', 'OFF']
boost_set = ['Weak', 'Strong']


# -- SORTING HATS -- #
n_class = random.choice(n_set)
gr_class = random.choice(gr_set)
slow_tyres = random.choice(slow_tyre_set)
fast_tyres = random.choice(fast_tyre_set)
damage_level = random.choice(damage_set)
boost_level = random.choice(boost_set)

# -- TOGGLES -- #

# Car Class/Category:
car_class_set = ['N', 'G']
car_cat = random.choice(car_class_set)

if car_cat == 'N': 
    car_class = (n_class)
else: 
    car_class = (gr_class)

# TYRES:
compound_set = ['SLOW', 'FAST']
compound = random.choice(compound_set)

if compound == 'SLOW':
    tyres = (slow_tyres)
else:
    tyres = (fast_tyres)

# -- OUTPUT -- #
print(f"Let's race {car_class}s on {tyres} with DAMAGE:[{damage_level}] and BOOST set to {boost_level}")

# https://pynative.com/python-random-choice/
