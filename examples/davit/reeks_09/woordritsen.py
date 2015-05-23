'''
Created on Mar 12, 2015

@author: david
'''
import re
import fileinput
def leesWoorden(bestandsnaam):
    returnvalue = set()
    for line in fileinput.input(bestandsnaam):
        returnvalue.add(line[:-1].upper())
    return returnvalue

def woordritsen(woord,woorden):
    reg = re.search("^([a-zA-Z]*)-(\.*)-([a-zA-Z]*)$",woord)
    prefix = reg.group(1).upper()
    firstwordlength = len(reg.group(2))+len(prefix)
    postfix = reg.group(3).upper()
    middlefixes = set()
    for woordje in woorden:
        if(len(woordje)!= firstwordlength):
            continue
        if(woordje.upper().startswith(prefix)):
            middlefixes.add(woordje.upper()[len(prefix):])
    truemiddlefixes = list() 
    for middlefix in middlefixes:
        samenstelling = middlefix + postfix
        if(samenstelling in woorden):
            if(middlefix is ""):
                continue
            truemiddlefixes.append(middlefix)
    returnstring = reg.group(1) + "-"
    if(len(truemiddlefixes) is 0):
        return returnstring +"???-"+reg.group(3)
    for middlefix in sorted(truemiddlefixes):
        returnstring = returnstring + middlefix + ","
    return returnstring[:-1] + "-"+reg.group(3)
        
        
print(woordritsen("veld-.....-veld",leesWoorden("woordenlijst.txt")))