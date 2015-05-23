'''
Created on Mar 20, 2015

@author: david
'''
import re
class Quilt:
    rotateMap = dict()
    rotateMap["/"] = "\\"
    rotateMap["\\"] = "/"
    rotateMap["+"] = "+"
    rotateMap["*"] = "*"
    rotateMap["|"] = "-"
    rotateMap["-"] = "|"
    rotateMap["o"] = "o"
    rotateMap["x"] = "x"
    
    allowChars = "/+*-\|ox"
    def __init__(self,rijen,kolommen,patroon):
        patroon = re.sub('\\\\\\\\','\\\\',patroon)
        if(len(patroon) != rijen * kolommen or not all(c in self.allowChars for c in patroon)):
            raise AssertionError("ongeldige configuratie")
        self.pattern = [patroon[i*kolommen:(i+1)*kolommen] for i in range(0, rijen)]
    
    def __str__(self):
        return "\n".join(self.pattern)
    
    def __repr__(self):
        patroon = re.sub('\\\\','\\\\\\\\',"".join(self.pattern))
        return "Quilt({}, {}, '{}')".format(len(self.pattern),len(self.pattern[0]),patroon)
    
    def draai(self):
        # this could easily be a one-liner, just substitute everywhere
        rijen = len(self.pattern[0])
        kolommen = len(self.pattern)
        text = ["".join([self.rotateMap[self.pattern[kolommen-1-j][i]] for j in range(kolommen)]) for i in range(rijen)]
        return Quilt(rijen,kolommen, "".join(text))
    
    def __add__(self,quilt):
        if(len(self.pattern) != len(quilt.pattern)):
            raise AssertionError("quilts zijn niet even hoog")
        # this could easily be a one-liner from here on, just substitute everywhere
        lijst = [self.pattern[i]+quilt.pattern[i] for i in range(len(self.pattern))]
        return Quilt(len(self.pattern),len(self.pattern[0])+len(quilt.pattern[0]),"".join(lijst))

print(repr(Quilt(2, 4, '//-\\++||')))

