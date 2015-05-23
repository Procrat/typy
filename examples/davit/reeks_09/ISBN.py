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
        
        """
        Hulpfunctie voor de berekening van het ISBN-13 controlecijfer
        """
        
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

def verwijder_tags(s):
    
    """
    Verwijdert alle XML tags uit een gegeven string en verwijdert daarna 
    witruimte vooraan en achteraan de string.
    
    >>> verwijder_tags(' <Title> The Practice of Computing using <b>Python</b> </Title> ')
    'The Practice of Computing using Python'
    """
    
    # verwijder alle XML tags uit de gegeven string
    s = s.strip()
    while s.find('<') >= 0:
        begin = s.find('<')
        einde = s.find('>')
        if einde == -1:
            einde = len(s)
        s = s[:begin] + s[einde+1:]
        
    # verwijder witruimte vooraan en achteraan en geef gewijzigde string terug
    return s.strip()

def printBoekInfo(code):
    
    """
    >>> printBoekInfo('9780136110675')
    Titel: The Practice of Computing using Python
    Auteurs: William F Punch, Richard Enbody
    Uitgever: Addison Wesley
    >>> printBoekInfo('9780136110678')
    Foutieve ISBN-13 code
    """
    
    # geldigheid van ISBN-13 code nagaan
    if not isISBN13(code):
        print('Foutieve ISBN-13 code')
        return
    
    # open webpagina met URL van ISBNdb.com die informatie oplevert over
    # opgegeven ISBN-13 code
    import urllib.request
    url = 'http://isbndb.com/api/books.xml'
    parameters = '?access_key=ZFD8L2Z5&index1=isbn&value1=' + code.strip()
    info = urllib.request.urlopen(url + parameters)

    # information over publicatie uit antwoord filteren en uitschrijven
    for regel in info:
        regel = regel.decode('utf-8')
        if regel.startswith('<Title>'):
            print('Titel: {}'.format(verwijder_tags(regel)))
        elif regel.startswith('<AuthorsText>'):
            print('Auteurs: {}'.format(verwijder_tags(regel).rstrip(', ')))
        elif regel.startswith('<PublisherText '):
            print('Uitgever: {}'.format(verwijder_tags(regel).rstrip(', ')))
            
    # webpagina afsluiten                       
    info.close()

if __name__ == '__main__':
    import doctest
    doctest.testmod()