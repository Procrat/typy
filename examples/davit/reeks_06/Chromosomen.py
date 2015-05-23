'''
Created on Feb 20, 2015

@author: david
'''
def crossoverpunten(chromosoom1,chromosoom2):
    teller1 = 0
    teller2 = 0
    aantal = 0
    while(teller1 < len(chromosoom1) and teller2 < len(chromosoom2)):
        if(chromosoom1[teller1] == chromosoom2[teller2]):
            aantal+= 1
            teller1 +=1
            teller2 +=1
        elif(chromosoom1[teller1] < chromosoom2[teller2]):
            teller1+=1
        else:
            teller2+=1
    return aantal

def maximaleSom(chromosoom1,chromosoom2):
    teller1 = 0
    teller2 = 0
    som1 = 0
    som2 =0
    totaalsom = 0
    while(teller1 < len(chromosoom1) and teller2 < len(chromosoom2)):
        if(chromosoom1[teller1] == chromosoom2[teller2]):          
            totaalsom += max(som1,som2) + chromosoom1[teller1]
            teller1 +=1
            teller2 +=1
            som1 = som2 = 0
        elif(chromosoom1[teller1] < chromosoom2[teller2]):
            som1 += chromosoom1[teller1]
            teller1+=1           
        else:
            som2 += chromosoom2[teller2]
            teller2+=1
    
    for i in range(teller1,len(chromosoom1)):
        som1+=chromosoom1[i]
        
    for i in range(teller2,len(chromosoom2)):
        som2+=chromosoom2[i]
        
    totaalsom += max(som1,som2)
    return totaalsom
chromosoom1 = [3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62]
chromosoom2 = [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]

print(maximaleSom(chromosoom1, chromosoom2))