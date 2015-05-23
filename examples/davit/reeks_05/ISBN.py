def isISBN(code):
    
    """
    Gaat na of de gegeven ISBN-10 code geldig is of niet.
    
    >>> isISBN('9971502100')
    True
    >>> isISBN('9971502108')
    False
    """
    
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

def controlecijfer(code):
    
    """
    >>> controlecijfer('997150210')
    '0'
    >>> controlecijfer('938389293')
    '5'
    """
        
    # controlecijfer berekenen
    controle = sum((i + 1) * int(code[i]) for i in range(9)) % 11
    
    # controlecijfer omzetten naar stringvoorstelling
    return 'X' if controle == 10 else str(controle)

if __name__ == '__main__':
    import doctest
    doctest.testmod()