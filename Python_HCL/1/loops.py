#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

x, n = input().split()

try:
    x = int(x)
except ValueError:
    print ('x nie liczba')

try:
    n = int(n)
except ValueError:
    print ('n nie integer')

i = 1
while i <= n:
    print(i*x)
    i = i +1