'''
Created on Mar 19, 2015

@author: david
'''
class BuzzBingo:
    def __init__(self,n,lijst):
        if(len(lijst)!= n**2):
            raise AssertionError("ongeldige kaart")
        self.card = list()
        for i in range(n):
            self.card.append(['-']*n)
        self.lijst = lijst
        self.n=n
    
    def __str__(self):
        return "\n".join(map((lambda x:"".join(x)),self.card))
    
    def __repr__(self):
        return str(self)
    
    def schrapWoord(self,woord):
        try: 
            index = self.lijst.index(woord)
        except:
            raise AssertionError("{} staat niet op de kaart".format(woord))
        rij = int(index / self.n)
        kolom = index % self.n
        if(self.card[rij][kolom] == "x"):
            raise AssertionError("{} is reeds geschrapt".format(woord))
        self.card[rij][kolom] = "x"
        return (rij,kolom)
    
    def schrapWoorden(self,woorden):
        return list(map((lambda x: self.schrapWoord(x)),woorden))
    
    def gewonnen(self):       
        for i in range(self.n):
            verticaal = True
            horizontaal = True
            for j in range(self.n):
                if(not verticaal and not horizontaal):
                    break
                horizontaal = horizontaal and self.card[i][j] == "x"
                verticaal = verticaal and self.card[j][i] == "x"
            if(verticaal or horizontaal):
                return True
        return False
            

bingo = BuzzBingo(4, [
   'cell', 'bacteria', 'PCR', 'virus', 
    'allele', 'chromosome', 'DNA', 'meiosis', 
    'protein', 'phenotype', 'gene', 'mutation',
    'genome', 'recessive', 'RNA', 'mitosis'
 ])

bingo.schrapWoord('phenotype')
print(bingo)
print(str(bingo.schrapWoorden(['PCR', 'chromosome', 'protein'])))
print(bingo.gewonnen())
print(bingo)
