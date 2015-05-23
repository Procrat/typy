'''
Created on Mar 6, 2015

@author: david
'''
def codeersleutel(sleutel):
    key = sleutel.replace(" ", "").upper()
    dict = {}
    for i in range(len(key)):
        if(key[i] in dict):
            dict[key[i]].append(i+1)
        else:
            dict[key[i]] = [i+1]
    return dict

def codeer(tekst, sleutel):
    key = codeersleutel(sleutel)
    indexes = dict.fromkeys(key, 0)
    result = []
    for i in tekst:
        char = i.upper()
        if(char in key):
            result.append(key[char][indexes[char]])
            indexes[char] = (indexes[char]+1)%len(key[char])
    return result
sleuteltekst = 'Lost time is never found again.'
print(codeer('nondeterminativeness', sleuteltekst))