#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

def zlozenie(n):
    def multi(func):
        def loop(x):
            for i in range (0, n):
                x = func(x)
            return x
        return loop
    return multi

@zlozenie(3)
def f1(x):
    return x+1

@zlozenie(2)
def f2(x):
    return x*x

@zlozenie(5)
def f3(word):
    return "".join(chr(ord(l)+1) for l in word)

print(f1(2)==5)
print(f2(3)==81)
print(f3("alamakota")=="fqfrfptyf")