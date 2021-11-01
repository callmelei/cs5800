# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 10:54:11 2021

@author: lei
"""

inputs = input().split(' ')

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

# reverse the exponents to start from the lowest power
exponents.reverse()

remainder = 1
temp = a
for i in range(len(exponents)):
    if i == 0: 
        temp = temp % n
    else:
        # square the remainder of last step
        temp = (temp**2) % n
    print(temp)
    
    if exponents[i] == 1:
        remainder = (remainder * temp) % n

print(remainder)