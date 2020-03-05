#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
import pandas
#1
data = pandas.read_csv('Meteorite_landings.csv')
# 2
data = data.dropna(how='any')
# 4
max_mass = data['mass (g)'].idxmax()
print ('Biggest: ')
print(data.loc[max_mass])

min_mass = data['mass (g)'].idxmin()
print ('\n\nSmallest: ')
print(data.loc[min_mass])

# 5
print ('\n\nmost meteorites seen falling in year: ')
groups = data.loc[data['fall']=='Fell'].groupby(['year']).size().idxmax()
print (groups)

# 6
print ('\n\nmost northern: ')
north = data.loc[data['reclat'].idxmax()]
print (north)

print ('\n\nmost southern: ')
south = data.loc[data['reclat'].idxmin()]
print (south)

# 7
print ('\n\nmost common location of meteorites: ')
groups = data.groupby(['GeoLocation']).size().idxmax()
print (groups)
