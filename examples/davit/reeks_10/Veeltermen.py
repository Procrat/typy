'''
Created on Mar 19, 2015

@author: david
'''
class Veelterm:
    def __init__(self,lijst):
        self.termen = list(lijst)
        while(len(self.termen) > 0 and self.termen[-1]==0):
            self.termen.pop()
            
    def __str__(self):
        result = ""
        if(len(self.termen) == 0):
            return "0"
        for i in range(len(self.termen)):
            if(self.termen[i] != 0):
                if(i == 0):
                    result += self._printFactor(i,False)
                elif( i == 1):
                    result += self._printFactor(i)+"x "
                else:
                    result += self._printFactor(i)+"x^{} ".format(i)
        if(result[0] =="+"):
            result = result[2:]
        return result[:-1]
    
    def _printFactor(self,i, multiplicate = True):
        result = ""
        if(self.termen[i] == 1):
            if(multiplicate):
                return "+ "
            return "+ 1 "
        if(self.termen[i] == -1):
            if(multiplicate):
                return "- "
            return "- 1 "
        if(self.termen[i] < 0):
            result = "- "+str(-self.termen[i])
        else: 
            result = "+ "+str(self.termen[i])
        if(multiplicate):
            return result + " * "
        return result
    
    def __repr__(self):
        return "Veelterm({})".format(self.termen)
    
    def __add__(self,term):
        if(len(self.termen) > len(term.termen)):
            short = term.termen
            long = self.termen
        else:
            short = self.termen
            long = term.termen
        lijst = list()
        for i in range(len(short)):
            lijst.append(short[i]+long[i])
        for i in range(len(short),len(long)):
            lijst.append(long[i])
        return Veelterm(lijst)
    
    def __neg__(self):
        return Veelterm(map((lambda x: -x),self.termen))
    
    def __sub__(self,term):
        return self + (-term)
    
    def __mul__(self,term):
        lijst = [0]*(len(self.termen)+len(term.termen))
        for i in range(len(self.termen)):
            for j in range(len(term.termen)):
                lijst[i+j] += self.termen[i]*term.termen[j]
        return Veelterm(lijst)
    
    def afgeleide(self):
        return Veelterm(list(x[0]*x[1] for x in enumerate(self.termen))[1:])

        
p = Veelterm([1, -1])
print(p.afgeleide())
q = Veelterm([0, 1, 0, 0, -6, -1])     
print(p-p) 