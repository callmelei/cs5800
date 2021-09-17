# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 10:54:11 2021

@author: lei
"""
import numpy as np

inputs = input('Enter inputs here: ')

inputs = inputs.split(' ')

a, b, n = int(inputs[0]), int(inputs[1]), int(inputs[2])

# compute binary form of the exponent
exponents = []
while b > 0:
    if b % 2 == 0:
        exponents.insert(0, 0)
    else:
        exponents.insert(0, 1)
    b //= 2

print(*exponents, sep='')

# squaring up
remainder = 1
val = 1
for i in range(len(exponents)):
    if i == 0:
        val *= a
    else:
        val *= val
    
    if exponents[i] == 1:
        print(val % n)
        remainder *= (val % n)

print(remainder % n)