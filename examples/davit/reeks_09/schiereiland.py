'''
Created on Mar 13, 2015

@author: david
'''
def landmassa(filename):
    connecties = 0
    landmassa = 0
    invoer = open(filename)
    inhoud = invoer.readlines()    
    inhoud = list(map((lambda x: list(x[:-1])),inhoud))
    for i in range(len(inhoud)):
        for j in range(len(inhoud[i])):            
            if(inhoud[i][j] == "S"):
                landmassa += 1
                continue
            if(inhoud[i][j] == " "):
                continue
            if(j != 0 and inhoud[i][j-1] == "S"):
                connecties += 1
                continue
            if(j != len(inhoud[i])-1 and inhoud[i][j+1] == "S"):
                connecties += 1
                continue
            if(i != 0  and inhoud[i-1][j] == "S"):
                connecties += 1
                continue
            if(i != len(inhoud)-1  and inhoud[i+1][j] == "S"):
                connecties += 1
                continue
    invoer.close()
    return (connecties,landmassa)

def landsoort(filename,verhouding=0.05):
    tupel = landmassa(filename)
    if(tupel[0] == 0):
        return "eiland"
    if(tupel[0]/tupel[1] <= verhouding):
        return "schiereiland"
    return "vasteland"
print(landmassa('landmassa1.txt'))
print(landsoort('landmassa1.txt',verhouding=0.01))