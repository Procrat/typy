'''
Created on Mar 3, 2015

@author: david
'''
def isISBN10(code):
    
    """
    Gaat na of de gegeven ISBN-10 code geldig is of niet.
    
    >>> isISBN10('9971502100')
    True
    >>> isISBN10('9971502108')
    False
    """
    
    def controlecijfer(code):
        
        # controlecijfer berekenen
        controle = sum((i + 1) * int(code[i]) for i in range(9)) % 11
    
        # controlecijfer omzetten naar stringvoorstelling
        return 'X' if controle == 10 else str(controle)

    # controleer of de gegeven code een string is
    if not isinstance(code, str):
        return False
    
    # controleer of de gegeven code bestaat uit 10 karakters
    if len(code) != 10:
        return False
    
    # controleer of de eerste negen karakters van de gegeven code cijfers zijn
    if not code[:9].isdigit():
        return False
    
    # controleer het controlecijfer van de gegeven code
    return controlecijfer(code) == code[-1]

def isISBN13(code):
    
    """
    Gaat na of de gegeven ISBN-13 code geldig is of niet.
    
    >>> isISBN13('9789743159664')
    True
    >>> isISBN13('9787954527409')
    False
    >>> isISBN13('8799743159665')
    False
    """
    
    def controlecijfer(code):
        
        # controlecijfer berekenen
        controle = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
    
        # controlecijfer omzetten naar één enkel cijfer
        return str((10 - controle) % 10)

    # controleer of de gegeven code een string is
    if not isinstance(code, str):
        return False
    
    # controleer of de gegeven code bestaat uit 13 karakters
    if len(code) != 13:
        return False
    
    # controleer of alle karakters van de gegeven code cijfers zijn
    if not code.isdigit():
        return False
    
    # controleer het controlecijfer van de gegeven code
    return controlecijfer(code) == code[-1]

def isISBN(code, isbn13=True):
    
    """
    >>> isISBN('9789027439642', False)
    False
    >>> isISBN('9789027439642', True)
    True
    >>> isISBN('9789027439642')
    True
    >>> isISBN('080442957X')
    False
    >>> isISBN('080442957X', False)
    True
    """
    
    return isISBN13(code) if isbn13 else isISBN10(code)
    
def zijnISBN(codes, isbn13=None):
    
    """
    >>> zijnISBN(
    ...     [
    ...         '0012345678', '0012345679', '9971502100', '080442957X',
    ...         5, True, 'The Practice of Computing Using Python',
    ...         '9789027439642', '5486948320146'
    ...     ]
    ... )
    [False, True, True, True, False, False, False, True, False]
    
    >>> zijnISBN(
    ...     [
    ...         '0012345678', '0012345679', '9971502100', '080442957X', 
    ...         5, True, 'The Practice of Computing Using Python', 
    ...         '9789027439642', '5486948320146'
    ...     ],
    ...     True
    ... )
    [False, False, False, False, False, False, False, True, False]
    
    >>> zijnISBN(
    ...     [
    ...         '0012345678', '0012345679', '9971502100', '080442957X', 
    ...         5, True, 'The Practice of Computing Using Python', 
    ...         '9789027439642', '5486948320146'
    ...     ],
    ...     False
    ... )
    [False, True, True, True, False, False, False, False, False]
    """
    
    # lijst met evaluaties initialiseren
    evaluaties = []
    
    # lijst met evaluaties opbouwen
    for code in codes:
        if isinstance(code, str):
            if isbn13 is None:
                if len(code) == 13:
                    evaluaties.append(isISBN(code, True))
                else:
                    evaluaties.append(isISBN(code, False))
            else:
                evaluaties.append(isISBN(code, isbn13))
        else:
            evaluaties.append(False)
            
    # lijst met evaluaties teruggeven
    return evaluaties

if __name__ == '__main__':
    import doctest
    doctest.testmod()