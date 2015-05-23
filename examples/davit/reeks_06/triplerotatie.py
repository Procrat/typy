'''
Created on Feb 20, 2015

@author: david
'''
def applyRotation(text,k1,k2,k3,f):
    kl1 = []
    kl2 = []
    kl3 = []
    lijst = []
    for i in range(len(text)):        
        char = text[i]
        if(not char.isalpha()):
            lijst.append((kl3,len(kl3),k3))
            kl3.append(i)
        elif(char.lower() <= "i"):
            lijst.append((kl1,len(kl1),k1))
            kl1.append(i)
        elif(char.lower() <= "r"):
            lijst.append((kl2,len(kl2),k2))
            kl2.append(i)
        else:
            lijst.append((kl3,len(kl3),k3))
            kl3.append(i)
    result =  ""
    for i in range(len(lijst)):
        tupel = lijst[i]
        result += text[tupel[0][f(tupel[1],tupel[2])%len(tupel[0])]]
    return result
    
def codeer(text,k1,k2,k3):
    return applyRotation(text,k1,k2,k3,(lambda x,y:x+y))
            
    

def decodeer(text,k1,k2,k3):
    return applyRotation(text,k1,k2,k3,(lambda x,y:x-y))

print(codeer('Nobody expects the Spanish Inquisition!', 2, 3, 1))
print(decodeer(codeer('Nobody expects the Spanish Inquisition!', 2, 3, 1), 2, 3, 1))
        