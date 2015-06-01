'''
Created on Mar 13, 2015

@author: david
'''


def filterPeptide(peptide,minlen = 0,maxlen=None,bevat=None,ontbreekt=None):
    if(len(peptide) < minlen):
        return False
    if(maxlen is not None and len(peptide)>maxlen):
        return False
    if bevat is not None:
        for char in bevat:
            if(char.lower() not in peptide and char.upper() not in peptide):
                return False
    if ontbreekt is not None:
        for char in ontbreekt:
            if(char.lower() in peptide or char.upper() in peptide):
                return False
    return True    

def filterPeptiden(invoer,uitvoer,minlen=0,maxlen=None,bevat=None,ontbreekt=None):
    infile = open(invoer)
    uitfile = open(uitvoer,'w')
    line = infile.readline()[:-1]
    while line:
        if(filterPeptide(line,minlen,maxlen,bevat,ontbreekt)):
            print(line,file=uitfile) 
        line = infile.readline()[:-1]        
    infile.close()
    uitfile.close()
filterPeptiden('peptiden.txt', 'gefilterd.txt', minlen=10, maxlen=20)
            