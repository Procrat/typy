'''
Created on Mar 5, 2015

@author: david
'''
def kleur2grijs(lijst):
    x = 0.299*lijst[0] + 0.587*lijst[1] + 0.114*lijst[2]
    if(isinstance(lijst[0],int)):
        x = x / 255
    return x

def apply(arg,Ffloat,Fint):
    if(isinstance(arg,int)):
        return Fint(arg)
    if(isinstance(arg,float)):
        return Ffloat(arg)
    if(isinstance(arg[0],int)):
        return [Fint(arg[0]),Fint(arg[1]),Fint(arg[2])]
    return [Ffloat(arg[0]),Ffloat(arg[1]),Ffloat(arg[2])]

def inverteer(arg):
    return apply(arg,(lambda x: 1-x),(lambda x: 255 -x))

def defaultConvert(arg):
    return apply(arg,(lambda x: x**2),(lambda x: (x/255)**2))


def converteerBitmap(bitmap,converter=defaultConvert):
    return list(map((lambda x: list(map(converter,x))),bitmap))

matrix = [[[10, 10, 10], [255, 255, 255]], [[8, 8, 8]]]
print(converteerBitmap(matrix)[0])
    