#-*- encoding:utf-8 -*-

'''
Created on 2018. 12. 25.

@author: wooyoun
'''
import math

a = -5
b = abs(a)
print(b)

c,d = divmod(13, 4)
print(c, d, sep =", ")

e = max(3, -2.5, 5.6)
print(e)

print(math.pi)

import random

print(random.randrange(0, 65536))

a = range(1, 6)
print(a)

a = range(100, 80, -5)
print(a)

a = math.fsum([5.5, 6.3, 2])
print(a)



