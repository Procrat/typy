'''
Created on Feb 17, 2015

@author: david
'''
def josephus(n, k):
    #zero is last person!
    lijst = list(range(n))
    start = 1
    for i in range(n-1):
        start = (start+k-1)%len(lijst)
        del lijst[start]
    return (lijst[0]+n)%n
print(josephus(12,3))