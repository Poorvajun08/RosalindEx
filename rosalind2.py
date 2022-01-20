#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 23:39:50 2021

@author: poorvajuneja
"""


with open('rosalind_rna.txt') as f:
	dna_seq = f.read()

def DNA_to_RNA(sequence):
    rna_sequence = sequence.replace('T', 'U')
    return rna_sequence

print(DNA_to_RNA(sequence = dna_seq))


with open('dnatorna_poorvaj.txt', 'w') as fh:
	fh.write((DNA_to_RNA(sequence = dna_seq)))