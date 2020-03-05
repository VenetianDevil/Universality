#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
def accepts(*types):
    def check_accepts(func):
        if not len(types) == func.__code__.co_argcount:
            raise TypeError
        def new_func(*args, **kwds):
            for (a, t) in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError
            return func(*args, **kwds)
        new_func.__name__ = func.__name__
        return new_func
    return check_accepts
		
@accepts(str)
def capitalize(word):
    return word[0].upper() + word[1:]

print(capitalize('ola') == 'Ola')

try:
    capitalize(2)
except TypeError:
    print(True)

@accepts(float, int)
def static_pow(base, exp):
    return base ** exp 

print(static_pow(2., 2) == 4.)
print(static_pow(2., exp=2) == 4.)
print(static_pow(base=2., exp=2) == 4.)

try:
    static_pow('x', 10)
except TypeError:
    print(True)
    
try:
    static_pow(2, 2.2)
except TypeError:
    print(True)