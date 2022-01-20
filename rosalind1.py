#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:32:08 2021

@author: poorvajuneja
"""

with open('rosalind_dna.txt') as f:
	dna_data = f.read()

nucleotide_count = []
for nucleotides in ['A', 'C', 'G', 'T']:
	nucleotide_count.append(str(dna_data.count(nucleotides)))

print(' '.join(nucleotide_count))

with open('nucleotidecount_poorvaj.txt', 'w') as fh:
	fh.write(' '.join(nucleotide_count))