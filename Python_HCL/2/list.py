#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

n = int(input())

List = []
i = 1
while i <= n:
    List.append(int(input()))
    i = i +1

print (sum(List))

i =0
difference = product = List[0]
for i in List[1:]:
    difference = difference - i
    product = product * i


print (difference)
print (product)
