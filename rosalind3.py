#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 00:29:30 2021

@author: poorvajuneja
"""




with open('rosalind_revc.txt') as file:
    DNA = file.read().rstrip()

def reverseComplement(sequence):
      '''
    this function will take in a string of dna sequence
    reverse the sequence and store it in a new variable
    will match it to its's complementary base and return
    the complementarty strand as a new string'
      '''

   


      reverse_complement = ''
      complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
      dna_reverse = sequence[::-1]
      for base in dna_reverse:
          reverse_complement += (complement.get(base, base))
          
      return reverse_complement


print(reverseComplement(sequence = DNA))

    
with open('dnaReverse_poorvaj.txt', 'w') as fh:
	fh.write(reverseComplement(sequence = DNA))
    
    
