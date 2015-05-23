def puntInEiland(eiland, x, y):
    return x < len(eiland) and y < len(eiland[x]) and x > 0 and y > 0

def raakpunt(eiland, x, y):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if abs(i) != abs(j) and puntInEiland(eiland, x + i, y + j) and eiland[x + i][y + j] is 'S':
                return True

    return False

def landmassa(filename):
    with open(filename, 'r') as f:
        eiland = f.readlines()

    nRaakpunten = 0
    opp = 0
    for x, li in enumerate(eiland):
        for y, c in enumerate(li):
             nRaakpunten += 1 if c is '#' and raakpunt(eiland, x, y) else 0
             opp += 1 if c is 'S' else 0
    return (nRaakpunten, opp)

def landsoort(filename, verhouding=0.05):
    raakpunten, oppervlakte = landmassa(filename)
    if raakpunten == 0:
        return 'eiland'
    return 'schiereiland' if raakpunten/oppervlakte <= verhouding else 'vasteland'
