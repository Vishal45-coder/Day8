# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:28:27 2020

@author: vishal
"""


n=int(input("Enter n value"))
o=0
e=0
for i in range(1,n+1):
    if(i%2==0):
        e=e+1    
print(f"no.of even numbers in {n} is {e}")        
    
o=n-e
print(f"no of odd numbers in {n} is {o}")