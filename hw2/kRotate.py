# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 21:36:14 2021

@author: lei
"""

def kRotate(A):
    l, r = 0, len(A) - 1
    while l < r:
        m = l + (r - l) // 2
        if(A[m] > A[r]):
            l = m + 1
        else:
            r = m
    return l

A = [4, 5, 1, 2, 3]
A = [9, 10, 11, 13, 15, 4, 6, 8]
print(kRotate(A))
        