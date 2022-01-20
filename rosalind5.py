#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:03:07 2021

@author: poorvajuneja
"""
dna_seq = ''
with open('rosalind_gc.txt') as f:
	seq = f.readlines()
for i in seq:    
    dna_seq += i
f.close()    
dna_seq = dna_seq.replace('\n','')
dna_seq = dna_seq.split('>')
keys = []
values = []
for sequence in dna_seq:
    keys.append(sequence[:13])
    values.append(sequence[13:])
    
seq_dict = dict(zip(keys,values))
#print(seq_dict)

def GC_content(sequence):
    count_GC = 0
    for nucleotide in sequence:
         if nucleotide == 'G' or nucleotide == 'C':
              count_GC += 1
    content_GC = count_GC/len(sequence)*100
    return content_GC
    
for key,value in seq_dict.items():
    print(seq_dict[value],'\n', GC_content(sequence = value))
    #print(GC_content(sequence = sequence))