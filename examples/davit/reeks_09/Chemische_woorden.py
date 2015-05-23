'''
Created on Mar 12, 2015

@author: david
'''
import re
import fileinput
def leesSymbolen(filename):
    verzameling = set()
    for line in fileinput.input(filename):
        if(fileinput.isfirstline()):
            continue
        verzameling.add(re.search('^[^\t]*\t([^\t]*)\t',line).group(1))
    return verzameling   
        
def langstePrefix(woord,prefixen):
    returnwaarde = ""
    lowerWoord = woord.lower()
    for prefix in prefixen:
        if lowerWoord.startswith(prefix.lower()):
            if(len(prefix) > len(returnwaarde)):
                returnwaarde = prefix
    return returnwaarde

def chemischWoord(woord,prefixen):    
    returnvalue = langstePrefix(woord, prefixen)
    if(returnvalue is ""):
        return ""
    woord = woord[len(returnvalue):]
    while(woord is not ""):
        prefix = langstePrefix(woord, prefixen)
        if(prefix  is ""):
            return ""
        returnvalue = returnvalue + "-" + prefix
        woord = woord[len(prefix):]
    return returnvalue
print(chemischWoord('katalyse',leesSymbolen("periodiek_systeem.txt")))