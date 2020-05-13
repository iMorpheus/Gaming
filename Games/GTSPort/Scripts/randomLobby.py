#!/usr/local/bin/Python3

import random

# -- INPUTS/VAR -- #
n_set = ['N100', 'N200', 'N300', 'N400', 'N500', 'N600', 'N700', 'N800', 'N900', 'N1000']
gr_set = ['GrB', 'Gr4', 'Gr3', 'Gr2', 'Gr1', 'GrX']
hard_tyre_set = ['CH', 'SH', 'RH']
soft_tyre_set = ['CS', 'SS', 'RS']
damage_set = ['Light', 'Strong']
boost_set = ['Weak', 'Strong']


# -- SORTING HATS -- #
n_class = random.choice(n_set)
gr_class = random.choice(gr_set)
hard_tyres = random.choice(hard_tyre_set)
soft_tyres = random.choice(soft_tyre_set)
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
compound_set = ['H', 'S']
compound = random.choice(compound_set)

if compound == 'H':
    tyres = (hard_tyres)
else:
    tyres = (soft_tyres)

# -- OUTPUT -- #
print(f"Let's race {car_class} cars on {tyres} with {damage_level} DAMAGE and BOOST set to {boost_level}")

# https://pynative.com/python-random-choice/
