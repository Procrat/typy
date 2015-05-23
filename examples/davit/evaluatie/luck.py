'''
Created on Mar 24, 2015

@author: david
'''
def spelbord(reeks,schermen=1):
    if(len(reeks)%schermen != 0):
        raise AssertionError('ongeldig spelbord')
    return [list(reeks[start:start+schermen]) for start in range(0,len(reeks),schermen)]

def prijs(patroon,stappen,prijzen,start=0,schermen=1):
    bord = spelbord(prijzen,schermen)
    som = sum(patroon)
    som *= stappen//len(patroon)
    scherm = stappen%schermen
    for i in range(stappen%len(patroon)):
        som += patroon[i]
    return bord[(start+som)%len(bord)][scherm]
        
prijzen=('$100', '$200', '$300', '$400', '$500', '$600', '$700', '$800', '$900', '$1000', 'whammy', '$1100', '$1200', '$1300', '$1400', '$1500')
print(spelbord(prijzen,schermen=2))  
print(prijs(start=1, 
            patroon=[1, 3, 7], 
            schermen=2, 
            prijzen=('$100', '$200', '$300', '$400', '$500', '$600', '$700', '$800', '$900', '$1000', 'whammy', '$1100', '$1200', '$1300', '$1400', '$1500'), 
            stappen=2))