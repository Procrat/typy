def eerste(hidato):
	for x in hidato:
		if min(x) == 1:
			return (hidato.index(x), x.index(1))

def opvolger(oplossing, rij, kolom):
	getal = oplossing[rij][kolom]
	for i in range(-1,2):
		for j in range(-1,2):
			if inRange(rij + i, oplossing) and inRange(kolom + j, oplossing[i]):
				if oplossing[rij + i][kolom + j] == getal + 1:
					return (rij + i, kolom + j)
	return (None, None)

def laatste(oplossing):
	t = eerste(oplossing)
	while opvolger(oplossing, t[0], t[1]) != (None, None):
		t = opvolger(oplossing, t[0], t[1])
	return t

def hidato(oplossing):
	oppervlakte = len(oplossing) * len(oplossing[0])
	tuple = laatste(oplossing)
	return oplossing[tuple[0]][tuple[1]] == oppervlakte

def inRange(x, y):
	return x < len(y)
			