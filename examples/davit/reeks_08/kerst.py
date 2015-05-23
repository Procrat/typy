'''
Created on Mar 6, 2015

@author: david
'''   
from random import shuffle
def isGeldigeTrekking(trekking,familie,zelfdeGezin=False):
    for gezin in familie:
        for persoon in gezin:
            if(trekking[persoon] == persoon):
                return False
            if(zelfdeGezin and trekking[persoon] in gezin):
                return False
    return True

def maakLijst(familie):
    lijst = []
    for gezin in  familie:
        lijst.extend(gezin)
    return lijst
def maakTrekking(familie):
    lijst = maakLijst(familie)
    shuffle(lijst)
    dictio = dict()
    for i in range(len(lijst)):
        dictio[lijst[i]] = lijst[(i+1)%len(lijst)]
    return dictio

def maakGeldigeTrekking(familie, zelfdeGezin=False):
    if(zelfdeGezin):
        while(True):
            trekking = maakTrekking(familie)
            if(isGeldigeTrekking(trekking,familie,True)):
                return trekking
    else:
        return maakTrekking(familie)
    
familie = ({'Alice', 'Bob', 'Cindy'}, {'Dora', 'Eric', 'Felix'})
print(maakGeldigeTrekking(familie, zelfdeGezin=True))