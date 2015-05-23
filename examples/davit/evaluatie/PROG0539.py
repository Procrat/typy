'''
Created on Mar 24, 2015

@author: david
'''
import re
def stamuitgang(uitspraak):
    match = re.search('^(.*) (..(1|2)[^12]*)$',uitspraak)
    if(match == None):
        return ('',uitspraak)
    return (match.group(1),match.group(2))

class Rijm:
    def __init__(self,bestandsnaam):
        self.woorden = dict()
        self.suffixes = dict()
        bestand = open(bestandsnaam)
        regel = bestand.readline()[:-1]
        while regel:
            if(regel[0]=="#"):
                regel = bestand.readline()[:-1]
                continue
            regel = re.sub(' +',' ',regel)
            regel = re.sub(' $','',regel)
            splitted = regel.split(' ',1)
            word = re.sub('\([0-9]*\)$','',splitted[0]).upper()
            if(word not in self.woorden):
                self.woorden[word] = set()
            self.woorden[word].add(splitted[1])  
            uitgang = stamuitgang(splitted[1])[1]
            if(uitgang not in self.suffixes):
                self.suffixes[uitgang] = set()   
            self.suffixes[uitgang].add(word)     
            regel = bestand.readline()[:-1]
            
    
    def uitspraken(self,woord):
        if(woord.upper() not in self.woorden):
            raise AssertionError("onbekend woord: {}".format(woord))
        return self.woorden[woord.upper()]
    
   
    def rijmen(self,woord1,woord2):
        suffixen1 = {stamuitgang(x)[1] for x in self.uitspraken(woord1)}
        suffixen2 = {stamuitgang(x)[1] for x in self.uitspraken(woord2)}
        for suffix1 in suffixen1:
            if(suffix1 in suffixen2):
                return True
        return False
    
    def rijmwoorden(self,woord):
        suffixes = [stamuitgang(x)[1] for x in self.uitspraken(woord)]
        result = set()
        for suffix in suffixes:
            result = result.union(self.suffixes[suffix])
        result.remove(woord.upper())
        return result
    
rijm = Rijm("woorden.txt")
print(rijm.rijmwoorden("STALIN'S"))
# print(stamuitgang({'S AY1 AH0 N S'}))