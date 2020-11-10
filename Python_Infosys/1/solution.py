#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
##########################################
# Write a program that reads one line from the the standard input which contains two integers and a symbol of the operation. Depending on the symbol, the program should print the correct value of the operation. If the user gave the wrong symbol, it should print text "Error".

# Input
# Space separated integers X and Y (-1000 ≤ X ≤ 1000, -1000 ≤ Y ≤ 1000) and a symbol of the operation S (+, -, *, %)

# Output
# Result of the operation X S Y

# Example
# Input:
# 4 3 +

# Output:
# 7
############################################

x, y, operand = input().split()

try:
    x = int(x)
except ValueError:
    print ('x nie liczba')

try:
    y = int(y)
except ValueError:
    print ('y nie integer')

if x >= -1000 and x <= 100 and y>=-1000 and y<=1000:
  if operand == '+':
    print(x + y)
  elif operand == '-':
    print(x - y)
  elif operand == '*':
    print(x * y)
  elif operand == '%':
    print(x % y)
  else:
    print('Error')