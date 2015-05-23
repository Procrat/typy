'''
Created on Mar 13, 2015

@author: david
'''
import random
def woordenlijst(filename):
    source = open(filename)
    inhoud = source.read()
    source.close()
    return inhoud.split()

def vervolgwoorden(lijst,k):
    mapje = dict()
    for i in range(k,len(lijst)):
        keys = tuple(lijst[i-k:i])
        if(keys in mapje):
            mapje[keys].append(lijst[i])
        else:
            mapje[keys] = [lijst[i]]
    return mapje

def nonsens(start,vervolg,minimumlengte,originalMinimumlength = None):
    if(originalMinimumlength is None):
        originalMinimumlength = minimumlengte
    if(start not in vervolg ):
        return ' '.join(start)
    
    popped=start[0]
    lijst = list(start)[1:]
    
    realMinimum = minimumlengte - len(start)
    
    nieuw = random.choice(vervolg[start])
    lijst.append(nieuw)
    nieuwStart = tuple(lijst)
    if((realMinimum <= 0 and nieuw[-1] in ("?","!",".")) or realMinimum <= 0 - originalMinimumlength):
        return popped + ' ' + ' '.join(nieuwStart)
    
    return popped + " "+ nonsens(nieuwStart,vervolg,minimumlengte-1,originalMinimumlength)
    
    
print(nonsens(('She', 'loves', 'you,'),vervolgwoorden(woordenlijst('shelovesyou.txt'),3),25))
