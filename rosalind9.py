#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:42:03 2021

@author: poorvajuneja
"""

with open('rosalind_subs.txt') as f:
    dataset = f.read()
    
def locations(datset):
    '''
    Given two DNA strings s and t the function
 will return all locations of t as a substring of s.
    '''

    results = []

    s, t = dataset.split()
    l = len(t)

    for i in range(len(s) - l):
        if s[i:i+l] == t:
            results.append(i + 1)

    return results

   
results = locations(dataset)
print(' '.join(map(str, results)))


with open('subset_poorvaj.txt','w') as fh:
    fh.write(' '.join(map(str, results)))