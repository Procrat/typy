def grandslam(prijzen):
	keys = list(prijzen)
	set = prijzen[keys[0]].copy()
	for x in range(1, len(keys)):
		set &= prijzen[keys[x]]
	return set

def uitslover(naam, prijzen):
	if(naam in grandslam(prijzen)):
		return 'ja'
	keys = list(prijzen)
	prijs = ""
	for x in keys:
		if naam not in prijzen[x]:
			if prijs == "":
				prijs = x
			elif prijs != "":
				return 'neen'
	return "bijna (geen {0})".format(prijs)