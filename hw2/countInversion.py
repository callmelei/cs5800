# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 11:08:49 2021

@author: lei
"""
# merge two intervals in sorted order and 
# return the number of qualified inversions
def merge(A, left, mid, right, t=1):
    count = 0
    
    tmp = [None] * (right - left + 1)
    
    i, j, k = left, mid + 1, 0
    
    while i <= mid and j <= right:
        if A[i] < A[j]:
            tmp[k] = A[i]
            i += 1
        else:
            tmp[k] = A[j]
            
            if A[i] > t * A[j]:
                # skip comparing for numbers after A[i]
                count += mid - i + 1
            else:
                idx = search(A, i + 1, mid, t * A[j])
                if(idx != -1):
                    count += mid - idx + 1
            
            j += 1
            
        k += 1
    
    while j <= right:
        tmp[k] = A[j]
        j += 1
        k += 1
    
    while i <= mid:
        tmp[k] = A[i]
        i += 1
        k += 1
    
    for p in range(left, right + 1):
        A[p] = tmp[p - left]
    
    return count

# mergeSort return the number of qualified inversions
def mergeSort(A, left, right, t):
    if left < right:
        mid = left + (right - left) // 2;
        count1 = mergeSort(A, left, mid, t)
        count2 = mergeSort(A, mid + 1, right, t)
        count3 = merge(A, left, mid, right, t)
        return count1 + count2 + count3
    else:
        return 0

# binary search
# return the index of the smallest number bigger than x
# return -1 if no number is bigger than x
def search(A, start, end, x):
    if A[end] <= x:
        return -1;
    
    while start < end:
        mid = start + (end - start) // 2
        if A[mid] <= x:
            start = mid + 1
        else:
            end = mid
    
    return start

# t = 1
# n = 6
# A = [12, 11, 13, 5, 6, 7]

t = 2
n = 4
A = [8, 4, 2, 1]
count = mergeSort(A, 0, n - 1, t)
print(count)