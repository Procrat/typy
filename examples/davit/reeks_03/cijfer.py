'''
Created on Feb 12, 2015

@author: david
'''
aantal = int(input())
for x in range(0,aantal):
    nummer = int(input())
    grootte = 1
    ondergrens = 0
    bovengrens = 9
    while bovengrens < nummer:
        ondergrens = bovengrens
        bovengrens += 9*(10**grootte)*(grootte+1)
        grootte += 1
    rest = nummer - ondergrens
    orde = (grootte - (rest % grootte))%grootte
    number = (rest -1) // grootte
    result =  (number // (10 ** orde))%10
    if(orde == grootte -1):
        result +=1
    print(result)