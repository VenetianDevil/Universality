#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#############################

# Write a program that will print only prime numbers from the given range

# Input
# Space separated integers X and Y ( 1 ≤ X < Y ≤ 10000)

# Output
# Space separated prime numbers from the range [X, Y]

# Example
# Input:
# 1 11

# Output:
# 2 3 5 7 11

#############################

x, y = input().split()

try:
    x = int(x)
except ValueError:
    print ('x nie liczba')

try:
  y = int(y)
except ValueError:
  print ('y nie integer')

if x < y and x >= 1 and y <= 10000:
  for i in range(x, y+1):
    if i>1:
      isNot = True
      for j in range(2, i):
        if i % j == 0:
          isNot = False
          break
      if isNot:
        print(i)
