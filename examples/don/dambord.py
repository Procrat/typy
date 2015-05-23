def letter2cijfers(char, *strings):
	for x in range(0,3):
		if char in strings[x]:
			return str(getLabel(x, strings[0])) + str(strings[x].index(char))

def cijfers2letter(cijfers, *strings):
	n = int(cijfers[-1])
	if len(cijfers) == 1:
		return strings[0][n]
	else:
		return strings[findRijFromLabel(cijfers[0], strings[0])][n]

def codeer(string, *codes):
	res = ''
	for x in string:
		res += letter2cijfers(x, codes[0], codes[1], codes[2])
	return res

def decodeer(string, *codes):
	cijfer1 = str(codes[0].find(' '))
	cijfer2 = str(codes[0].find(' ', int(cijfer1) + 1))
	res = ''
	while len(string) > 0:
		temp = ''
		if string[0] == cijfer1:
			temp = cijfer1
			string = string[1:]
		elif string[0] == cijfer2:
			temp = cijfer2
			string = string[1:]
		res += cijfers2letter(temp + string[0], codes[0], codes[1], codes[2])
		string = string[1:]
	return res

def getLabel(rij, string):
	if rij == 0:
		return ''
	space = string.find(' ')
	for x in range(1,3):
		if rij == x:
			return space
		space = string.find(' ', space + 1)

def findRijFromLabel(cijfer, string):
	label = int(cijfer)
	res = int(string.find(' ') != label)
	return res + 1
