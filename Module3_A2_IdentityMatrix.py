# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 19:07:52 2020

@author: vishal
"""


n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()