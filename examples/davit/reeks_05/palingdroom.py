'''
Created on Feb 17, 2015

@author: david
'''
import math
def palindromisch(getal):
    return (getal == int(str(getal)[::-1]))
def palindroomveelvouden(n,c):
    count = 0
    for i in range((int(math.pow(10,c-1))-1)//n +1,(int(math.pow(10,c))-1)//n +1):
        if(palindromisch(i*n)):
            count += 1
    return count