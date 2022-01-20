#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 13:06:56 2021

@author: poorvajuneja
"""
with open('rosalind_hamm.txt') as f:
	data = f.readlines()

mutations_count = 0 # initialize mutations

# iterate through the sequences

for nucleotide in range(len(data[0])):
    if data[0][nucleotide] != data[1][nucleotide]:
        mutations_count += 1

print(mutations_count)

with open('mutationCount_poorvaj.txt', 'w') as fh:
	fh.write(str(mutations_count))  