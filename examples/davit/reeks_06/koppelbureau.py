'''
Created on Feb 20, 2015

@author: david
'''
def koppelbureau(mannen,vrouwen):
    aantal= len(mannen)
    rejected = [[False]*aantal]*aantal
    Vkoppels = [None]*aantal # map vrouw to man
    Mkoppels = [None]*aantal # reverse
    happy_men = list(range(aantal))
    while(len(happy_men) != 0):
        husband = happy_men.pop()
        for i in range(aantal):
            wife = mannen[husband][i]
            if(rejected[husband][wife]):
                continue
            preferences_wife = vrouwen[wife].index(husband)
            if(Vkoppels[wife] == None):
                Vkoppels[wife] = husband
                Mkoppels[husband] = (husband,wife)
                break
            elif(vrouwen[wife].index(Vkoppels[wife]) > preferences_wife):
                happy_men.append(Vkoppels[wife])
                Mkoppels[Vkoppels[wife]]= None #actually not necessary, pure semantics
                Vkoppels[wife] = husband
                Mkoppels[husband] = (husband,wife)
                break;
    return tuple(Mkoppels)
print(koppelbureau(
                   [[1, 0, 2, 3], [3, 0, 1, 2], [0, 2, 1, 3], [1, 2, 0, 3]], 
                   [[0, 2, 1, 3], [2, 3, 0, 1], [3, 1, 2, 0], [2, 1, 0, 3]]
                   ))
                
            
        
    