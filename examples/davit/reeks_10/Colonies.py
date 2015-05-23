'''
Created on Mar 20, 2015

@author: david
'''
class Petrischaal:
    def __init__(self,bestand):
        invoer = open(bestand)
        bitmap = invoer.readlines()
        self.bitmap = [list(x)[:-1] for x in bitmap]
        
    def __str__(self):
        return "\n".join(["".join(lijn) for lijn in self.bitmap])
    
    def kolonie(self,rij,kolom):
        if(self.bitmap[rij][kolom]==" "):
            raise AssertionError('geen kolonie gevonden op positie ({}, {})'.format(rij,kolom))
        return self._recurviseKolonie(rij, kolom)
        
    def _recurviseKolonie(self,rij,kolom):
        if(self.bitmap[rij][kolom]!= "#"):
            return 0
        count  = 1
        self.bitmap[rij][kolom]="."
        if(rij != 0):
            count += self._recurviseKolonie(rij-1, kolom)
        if(rij != len(self.bitmap)-1):
            count += self._recurviseKolonie(rij+1, kolom)
            
        if(kolom != 0):
            count += self._recurviseKolonie(rij, kolom-1)
        if(kolom != len(self.bitmap[rij])-1):
            count += self._recurviseKolonie(rij, kolom+1)
        return count
    
    def ongedaan_maken(self):
        for i in self.bitmap:
            for j in range(len(i)):
                if i[j] == ".":
                    i[j] = "#"
    
    def aantal(self,minimum = 1, functie = (lambda args,size: args+1), args = 0):
        # markeer kolonies aan de rand
        for i in range(len(self.bitmap)):
            self._recurviseKolonie(i, 0)
            self._recurviseKolonie(i, len(self.bitmap[i])-1)
        for i in range(len(self.bitmap[0])):
            self._recurviseKolonie(0, i)
            self._recurviseKolonie(len(self.bitmap)-1, i)
        
        # tel nu de andere
        for i in range(1,len(self.bitmap)-1):
            for j in range(1,len(self.bitmap[0])-1):
                size = self._recurviseKolonie(i, j)
                if(size  >= minimum ):
                    args = functie(args,size)
                    
        self.ongedaan_maken()    
        return args   
    
    def grootte(self,minimum =1):
        result = self.aantal(minimum,(lambda args,size:[args[0]+1,(args[0]*args[1]+size)/(args[0]+1)]),[0,0])[1]
        if result == 0:
            return None
        return result
schaal = Petrischaal('schaal.txt')
print(schaal.kolonie(10, 35))
schaal.ongedaan_maken()
print(schaal.grootte(1000))
