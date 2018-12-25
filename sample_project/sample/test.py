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

print("hello world"[3:-2])

print("hello world"[-1:0:-1])

age = 30
new_age = age + 10
print("10년 후 " + str(new_age))

text = str(573)
rev_text = text[-1::-1]
print(rev_text)





