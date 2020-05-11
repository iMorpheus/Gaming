
#!/usr/local/bin/Python3

import random

# SETS
country_set = ['US', 'GB', 'KR', 'IT', 'FR', 'GER', 'JP']
class_set = ['N100', 'N200', 'N300', 'N400', 'N500', 'N600', 'N700', 'N800', 'N900', 'N1000', 'GrB', 'Gr4', 'Gr3', 'Gr2', 'Gr1', 'GrX']
tyre_set = ['CH', 'SH', 'RH']
damage_set = ['Light', 'Strong']
boost_set = ['Weak' 'Strong']


# RANDOMIZE
country_code = random.choice(country_set)
car_class = random.choice(class_set)
tyres = random.choice(tyre_set)
damage_level = random.choice(damage_set)
boost_level = random.choice(boost_set)

# PRINT
print("Country: ", country_code)
print("Class: ", car_class)
print("Tyres: ", tyres)
print("Damage: ", damage_level)
print("Boost: ", boost_level)

# https://pynative.com/python-random-choice/
