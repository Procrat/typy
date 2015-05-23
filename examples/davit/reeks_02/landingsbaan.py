'''
Created on Feb 12, 2015

@author: david
'''
coord = float(input())
coord += 5
first = coord // 10
second = (first + 18)%36
if first == 0 or second == 0:
    first = 18
    second = 36
elif second < first:
    temp = second
    second = first
    first = temp

print("%02d/%02d"%(first,second))