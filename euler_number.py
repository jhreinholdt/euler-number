"""
Created on Mon Sep 18 11:30:15 2017

@author: jorei
"""
#Find e to the Nth Digit.  
#Enter a number and have the program generate e up to that many decimal places. 
#Keep a limit to how far the program will go.
import math as ma

def eulernumber(Nth):
    print("Newton's Series Expansion for e =", '{:.{}f}'.format(newtoneexpansion(20), Nth))
    print("Brothers Formulae for         e =", '{:.{}f}'.format(brothersformulae(20), Nth))
    print("Math.e value for              e =", '{:.{}f}'.format(ma.e, Nth))
    
def newtoneexpansion(numb):
    enewton = 0
    n = 0
    while n <= numb:
        enewton += 1 / (ma.factorial(n))
        n += 1
    return enewton
    
def brothersformulae(num):
    ebrother = 0
    k = 0
    while k <= num:
        ebrother += (2*k + 2) / ma.factorial(2*k + 1)
        k += 1
    return ebrother    
    
def main():
    precision = 15
    eulernumber(precision)
    
if __name__ == '__main__':
    main()