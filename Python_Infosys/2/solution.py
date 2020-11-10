#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

#####################################
# Write a program to sum all of the elements in the given list of numbers.

# Input
# N (1 ≤ N ≤ 1000) space separated integers

# Output
# The sum of all the elements in the list

# Example
# Input:
# 2 0 1 3 5 9 -1

# Output:
# 19
#######################################

numbers = input().split()

summary = 0
for x in numbers:
  summary = summary + int(x)

print(summary)