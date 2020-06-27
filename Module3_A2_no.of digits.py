# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:56:57 2020

@author: vishal
"""


n=int(input("Enter a number"))
count=0
while(n>0):
    n=n//10
    count=count+1
print(f"The no.of digits in {n} is {count}")    