'''
Created on Mar 19, 2015

@author: david
'''
class Combinatieslot:
    def __init__(self,reeks,maxwaarde=9):
        self.oplossing = tuple(reeks)
        self.max = maxwaarde
        if(len(reeks)==0):
            raise AssertionError('ongeldige combinatie')
        for i in reeks:
            if(i > maxwaarde or i < 0):
                raise AssertionError('ongeldige combinatie')
        self.huidig = [0]*len(reeks)
    def __repr__(self):
        return 'Combinatieslot({}, maxwaarde={})'.format(self.oplossing,self.max)
    
    def __str__(self):
        return '-'.join(map(str,self.huidig))
    
    def roteer(self,schijven,posities):
        if(isinstance(schijven,int) ):
            if(schijven >= len(self.oplossing) or schijven < 0):
                raise AssertionError('ongeldige schijf')
            self.huidig[schijven] = (self.huidig[schijven] + posities)%(self.max+1)
            return
        
        for schijf in schijven:
            if(schijf >= len(self.oplossing) or schijf < 0):
                raise AssertionError('ongeldige schijf')
        for schijf in schijven:
            self.huidig[schijf] = (self.huidig[schijf] + posities)%(self.max+1)
            
    def open(self):
        for i in range(len(self.oplossing)):
            if(self.oplossing[i] != self.huidig[i]):
                return False
        return True

slot = Combinatieslot((9, 2, 4))
print(repr(slot))
print(slot)
slot