'''
Created on Feb 17, 2015

@author: david
'''
def combisom(lijst, getal):
    for i in range(0,len(lijst)):
        for j in range(0,len(lijst)):
            if(i != j and lijst[i]+lijst[j] == getal):
                return True
    return False

'''
def combisom(lijst, getal):
    if(getal == 0):
        return True
    if(len(lijst)==0):
        return False
    lijst = lijst[:]
    getal2 = lijst.pop()
    return (combisom(lijst,getal) or combisom(lijst, getal-getal2))
print(combisom([-37, 24, -3, 50, 3, 45, 40, 23, -11, 25, 36, -32, 21, 42], -47))
'''