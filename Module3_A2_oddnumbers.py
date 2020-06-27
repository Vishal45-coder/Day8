# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:51:25 2020

@author: vishal
"""


n=int(input("Enter a number"))
print(f"odd numbers in {n} is")
for i in range(1,n+1):
    if(i%2!=0):
        print(i)