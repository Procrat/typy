import random
import re

def woordenlijst( file ):
	fo = open(file)
	str = fo.read();
	return (str.split())
	close(file)
	
def vervolgwoorden( wlijst, k ):
	dict = {}
	for i in range(len(wlijst)-k):
		value = []
		key = ' '.join(wlijst[i:i+k])
		if key in dict:
			dict[key].append(wlijst[i+k])
		else:
			value.append(wlijst[i+k])
			dict[key] = value
	return dict

def nonsens( start, vervolg, minimumlengte ):	
	sentence = []
	punct = set('.?!')
	for s in start:
		sentence.append(s)
	x = 0
	while (x <= 2*minimumlengte):
		lastword = sentence[len(sentence)-1]
		lastchar = lastword[len(lastword)-1]
		if lastchar in punct and x >= minimumlengte:
			break  
		woord = ' '.join(start)
		if not woord in vervolg:
			break
		nextlist = vervolg[woord]
		nextword = nextlist[random.randrange(0, len(nextlist), 1)]
		sentence.append(nextword)
		start.append(nextword)
		start.remove(start[0])
		x += 1
	out = ' '.join(sentence)		
	return out

lijst=woordenlijst("Luke.txt")
print(lijst)
