def isISBN13(code):
    
    """
    Gaat na of de gegeven ISBN-13 code geldig is of niet.
    
    >>> isISBN13('9789743159664')
    True
    >>> isISBN13('9787954527409')
    False
    >>> isISBN13('8799743159664')
    False
    """
    
    def controlecijfer(code):
        
        # controlecijfer berekenen
        controle = sum((2 * (i % 2) + 1) * int(code[i]) for i in range(12))
    
        # controlecijfer omzetten naar één enkel cijfer
        return str((10 - controle) % 10)

    # controleer of de gegeven code een string is
    if not isinstance(code, str):
        return False
    
    # controleer of de gegeven code bestaat uit 13 karakters
    if len(code) != 13:
        return False
    
    # prefix van de gegeven code controleren
    if code[:3] not in {'978', '979'}:
        return False
    
    # controleer of alle karakters van de gegeven code cijfers zijn
    if not code.isdigit():
        return False
    
    # controleer het controlecijfer van de gegeven code
    return controlecijfer(code) == code[-1]

def overzicht(codes):
    
    """
    >>> codes = [
    ...    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
    ...    '9780817481461', '9785130738708', '9798810365062', '9795345206033', 
    ...    '9792361848797', '9785197570819', '9786922535370', '9791978044523', 
    ...    '9796357284378', '9792982208529', '9793509549576', '9787954527409', 
    ...    '9797566046955', '9785239955499', '9787769276051', '9789910855708', 
    ...    '9783807934891', '9788337967876', '9786509441823', '9795400240705', 
    ...    '9787509152157', '9791478081103', '9780488170969', '9795755809220', 
    ...    '9793546666847', '9792322242176', '9782582638543', '9795919445653', 
    ...    '9796783939729', '9782384928398', '9787590220100', '9797422143460', 
    ...    '9798853923096', '9784177414990', '9799562126426', '9794732912038', 
    ...    '9787184435972', '9794455619207', '9794270312172', '9783811648340', 
    ...    '9799376073039', '9798552650309', '9798485624965', '9780734764010', 
    ...    '9783635963865', '9783246924279', '9797449285853', '9781631746260', 
    ...    '9791853742292', '9781796458336', '9791260591924', '9789367398012' 
    ... ]
    >>> overzicht(codes)
    Engelstalige landen: 8
    Franstalige landen: 4
    Duitstalige landen: 6
    Japan: 3
    Russischtalige landen: 7
    China: 8
    Overige landen: 11
    Fouten: 9
    """
        
    # histogram van groepen opbouwen
    groepen = {}
    for i in range(11): 
        groepen[i] = 0
    for code in codes:
        if not isISBN13(code):
            groepen[10] += 1
        else:
            groepen[int(code[3])] += 1
        
    # samenvatting uitschrijven
    print('Engelstalige landen: {}'.format(groepen[0] + groepen[1]))
    print('Franstalige landen: {}'.format(groepen[2]))
    print('Duitstalige landen: {}'.format(groepen[3]))
    print('Japan: {}'.format(groepen[4]))
    print('Russischtalige landen: {}'.format(groepen[5]))
    print('China: {}'.format(groepen[7]))
    print('Overige landen: {}'.format(groepen[6] + groepen[8] + groepen[9]))
    print('Fouten: {}'.format(groepen[10]))
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()