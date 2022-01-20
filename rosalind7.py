#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 11:40:22 2021

@author: poorvajuneja
"""
with open('rosalind_iprb.txt') as f:
    data_allele = f.readline()
    
k,m,n = data_allele[:2:1],data_allele[3:5:1],data_allele[6:8:1]

    
    
def prob_dom(k,m,n):
    '''
    this function will take in following parameters:-
    k=homozygous dominant
    m=heterozygous recessive
    n= homozygous recessive
    
    and then will return us the probability that two random organisms
    that will produce individual with a dominant allele
    
    
    '''


    k,m,n = map(float, (k,m,n))
    total = k+m+n
    prob_m = m/total
    prob_n = n/total


    res_prob = 1 # Maximum probability   
    res_prob -= prob_n*((n-1)/(total-1))#if both homozygous recessive then subtract probabilities

    
    res_prob -= 2*prob_n*(m/(total-1))*0.5#for doubles

   
    res_prob -= prob_m*((m-1)/(total-1))*0.25 # if both heterozygous recessive subtract prob 

    return res_prob


print(prob_dom(k,m,n))
with open('medelLaw_poorvaj.txt', 'w') as fh:
	fh.write(str(prob_dom(k,m,n))) 