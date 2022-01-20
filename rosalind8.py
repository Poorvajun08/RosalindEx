#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 12:02:16 2021

@author: poorvajuneja
"""


with open('rosalind_prot.txt') as f:
    rna_seq = f.readline()
    




def codon_breaker(rna_seq):
        '''
       this function will break the string RNA Sequence
       and make it into list of codons by breaking it 
       by every third element
       
        '''  
        codon_lst =[]
        for i in range(0, len(rna_seq),3):
            codon_lst.append(rna_seq[i:i+3])
        return codon_lst
    
def codon_converter(codon_lst):
       '''
       this function will convert codon list file generated 
       by above function into its translated protein
       respectivley by using the mapping and store it in a list
       
       '''
       proteinlist_seq = []
       mapping = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
     "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
     "UAU":"Y", "UAC":"Y", "UAA":"stop", "UAG":"stop",
     "UGU":"C", "UGC":"C", "UGA":"stop", "UGG":"W",
     "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
     "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
     "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
     "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
     "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
     "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
     "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
     "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
     "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
     "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
     "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
     "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
       for j in codon_lst:
            if j in mapping.keys():
                proteinlist_seq.append(mapping.get(j))
       return proteinlist_seq



codon = codon_breaker(rna_seq)
protein = codon_converter(codon)

protein_string = ''
for k in protein: 
        protein_string += k  
print(protein_string)        

with open('protein_poorvaj.txt','w') as fh:
    fh.write(protein_string)


