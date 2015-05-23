'''
Created on Mar 6, 2015

@author: david
'''

def molecuulformule(structuurformule):
    old = ""
    lijst = {}
    for char in structuurformule:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if(old != ""):
                if(old in lijst):
                    lijst[old] = lijst[old] +1
                else:
                    lijst[old] = 1
            old =  char
        elif char in "abcdefghijklmnopqrstuvwxyz":
            old = old + char
    if(old in lijst):
        lijst[old] = lijst[old] +1
    else:
        lijst[old] = 1
    return lijst

def isomeren(struct1, struct2):
    return (molecuulformule(struct1) == molecuulformule(struct2))

structuurformule1 = 'OCaOSeOO'
structuurformule2 = 'HHCHHCHHCHHCHH'
structuurformule3 = 'HHCHHHCCHHHCHH'



print(isomeren(structuurformule2, structuurformule3))
