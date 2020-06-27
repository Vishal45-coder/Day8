# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:47:47 2020

@author: vishal
"""


n=int(input("enter a number"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)