def codeersleutel(sleuteltekst):
	dict = {}
	kopie = sleuteltekst.replace(' ','')
	lijst = list(enumerate(kopie))
	for x in lijst:
		if x[1] != ' ':
			letter = x[1].capitalize()
			if letter not in dict:
				dict[letter] = []
			dict[letter].append(1 + x[0])
	return dict

def codeer(tekst, sleuteltekst):
	lijst = []
	sleutel = codeersleutel(sleuteltekst)
	for x in tekst:
		letter = x.capitalize()
		lijst.append(sleutel[letter][0])
		sleutel[letter] = roteer(sleutel[letter])
	return lijst

def roteer(lijst):
    return lijst[1:] + lijst[:1]