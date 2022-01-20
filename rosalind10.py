#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:51:16 2021

@author: poorvajuneja
"""



with open('rosalind_subs.txt') as f:
    sequences = f.read[::1]





def base(matrix):
    strings = matrix.split()

    default = [0] * len(strings[0])
    results = { 'A': default[:],'C': default[:],'G': default[:],'T': default[:]}

    for nucleotide in strings:
        for i, j in enumerate(nucleotide):
            result1[j][i] += 1

    return result1


def consensus(profile):
    output = []

    keys = base.keys()

    for i in range(len(base[keys[0]])):
        max_v = 0
        max_k = None
        for k in keys:
            v = base[k][i]
            if v > max_v:
                max_v = v
                max_k = k
        output.append(max_k)

    return (''.join(output))



baseMatrix = base(sequences)
consensusMatrix = consensus(baseMatrix)
print(consensusMatrix)
for k in sorted(baseMatrix.iterkeys()):
    print("%s: %s" % (k, ' '.join(map(str, baseMatrix[k]))))
    

