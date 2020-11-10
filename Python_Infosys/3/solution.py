#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#############################

# Write a program that reads an integer and checks if the given number is a prime number or not. If the test is positive program should print "Yes" if not "No", if the given number is less than 2, the program should print "Error".

# Input
# An integer X (-100000 ≤ X ≤ 100000)

# Output
# Error - if X < 2
# No - if X > 1 and is not a prime number
# Yes - if X is a prime number
# Example
# Input:
# 61

# Output:
# Yes

#############################

x = input()

try:
    x = int(x)
except ValueError:
    print ('x nie liczba')

if x >= -100000 and x <= 100000:
  if x < 2:
    print('Error')
  else:
    isNot = True
    for i in range(2, x):
      if x % i == 0:
        print ('No')
        isNot = False
        break
    if isNot:
      print('Yes')