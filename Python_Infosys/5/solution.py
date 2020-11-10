#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#####################################

# You are given the following dictionary:

# car = { 
#   "brand": "Subaru", 
#   "model": "Impreza WRX STI", 
#   "power": "265hp", 
#   "year": 2007
# }
# Write a program that reads actions and then performs them on the given dictionary.

# Input
# The first line of input file contains a single positive integer N (N < 500) which is the number of actions to be performed on the given dictionary. The following N lines describe each action:

# PRINT KEY - prints the value of a key (if the key is in dictionary). If not, it prints NOT FOUND,
# SET KEY VALUE - sets the value of a key. Prints nothing,
# POP KEY - removes and prints an element from the dictionary having the given key (if the key is in dictionary). If not, it prints NOT FOUND,
# CLEAR - removes all items from the dictionary. Prints nothing.
# Example
# Input:
# 5
# PRINT model
# PRINT year
# SET year 2008
# PRINT year
# PRINT engine

# Output:
# Impreza WRX STI
# 2007
# 2008
# NOT FOUND

#####################################

car = { 
  "brand": "Subaru", 
  "model": "Impreza WRX STI", 
  "power": "265hp", 
  "year": 2007
}

n = int(input())

i = 0
commands = []
while i < n:
  commands.append(input())
  i = i+1

i = 0
while i < n:
  data = commands[i].split()
  if data[0] == 'PRINT':
    try:
      print(car[data[1]])
    except KeyError:
      print('NOT FOUND')
  elif data[0] == 'SET':
    car[data[1]] = data[2]
  elif data[0] == 'POP':
    try:
      print(car.pop(data[1]))
    except KeyError:
      print('NOT FOUND')
  elif data[0] == 'CLEAR':
    car.clear()
  i = i + 1
  