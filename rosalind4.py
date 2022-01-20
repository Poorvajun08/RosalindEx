#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 15:08:06 2021

@author: poorvajuneja
"""


# n - number of months
# k - number of pairs in litter
with open('rosalind_fib.txt') as f:
	data = f.read().rstrip().split(' ')
ints = [int(item) for item in data]

    

def fib(n,k):
    # total number of rabbit pairs
    rabbitA,rabbitB = 1,1
    for i in range(n-1):
        rabbitA,rabbitB = rabbitB, rabbitB+(rabbitA*k)
    return rabbitA

# using a list function to return all values
def fib_list(n,k):
    fib_table = []
    for i in range(n):
        if i < 2:
            fib_table.append(1)
        else:
            fib_table.append(fib_table[-1] + fib_table[-2]*k)
    return fib_table


print(fib(ints[0],ints[1]))
print(fib_list(ints[0],ints[1]))

with open('fibrabbits_poorvaj.txt', 'w') as fh:
	fh.write(str(fib(ints[0],ints[1])))  