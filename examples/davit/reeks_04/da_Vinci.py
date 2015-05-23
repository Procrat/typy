'''
Created on Feb 17, 2015

@author: david
'''
n = int(input())
for i in range(0,26):
    print(chr(ord('a') + i) + ' ' + str(n)[::-1])
    n = n << 1