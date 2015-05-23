'''
Created on Mar 3, 2015

@author: david
'''
import re
from datetime import date
def dmj(datum):
    return (int(re.search('^([0-9]*)[^0-9]',datum).group(1)),
            int(re.search('[^^0-9]([0-9]*)[^0-9]',datum).group(1)),
            int(re.search('[^^0-9]([0-9]*)$',datum).group(1)))

def verstreken(datum):
    t = dmj(datum)
    d0 = date(1970,1,1)
    d1 = date(t[2],t[1],t[0])
    return (d1 - d0).days

def mayadatum(datum,scheidingsteken=None):
    if(scheidingsteken ==  None):
        scheidingsteken = re.search('^[0-9]*([^0-9])',datum).group(1)
    dagen = verstreken(datum)
    pkin = 5 + dagen
    result = str(pkin%20)
    puinal = 7+ (pkin // 20)
    result = str(puinal % 18) + scheidingsteken + result
    ptun = 16+ (puinal // 18)
    result = str(ptun % 20) + scheidingsteken + result
    pkatun= 17+(ptun // 20)
    result = str(pkatun % 20) + scheidingsteken + result
    return str(pkatun // 20 +12) + scheidingsteken + result
print(mayadatum('01/01/1970'))