class ISBN13:
    
    """
    >>> code = ISBN13(9780136110675)
    >>> print(code)
    978-0-13611067-5
    >>> code
    ISBN13(9780136110675, 1)
    >>> code.isGeldig()
    True
    >>> code.alsISBN10()
    '0-13611067-3'
    """
    
    def __init__(self, code, lengte=1):

        # controleer geldigheid van argumenten        
        assert isinstance(code, int), 'ISBN13-codes moeten aangemaakt worden met integers.'
        assert len(str(code)) == 13, 'ISBN13-codes moeten 13 cijfers bevatten.'
        assert 1 <= lengte <= 5, 'ISBN13-codes hebben een landaanduiding tussen 1 en 5 cijfers.'
        
        self.code = code
        self.lengte = lengte
        
    def __str__(self):
        
        code = str(self.code)
        return '{}-{}-{}-{}'.format(
            code[:3], 
            code[3:3 + self.lengte], 
            code[3 + self.lengte:-1], 
            code[-1]
        )
    
    def __repr__(self):
        
        return 'ISBN13({}, {})'.format(self.code, self.lengte)
    
    def isGeldig(self):
        
        def controlecijfer(code):
            
            # ISBN-13 controlecijfer berekenen
            controle = sum((2 * (i % 2) + 1) * int(code[i]) for i in range(12))
        
            # controlecijfer omzetten naar stringvoorstelling
            return str((10 - controle) % 10)

        # ISBN13-code omzetten naar string
        code = str(self.code)
        
        # nagaan of controlecijfer geldig is
        return code[12] == controlecijfer(code)        
        
    def alsISBN10(self):
        
        def controlecijfer(code):
            
            # ISBN-10 controlecijfer berekenen
            controle = sum((i + 1) * int(code[i]) for i in range(9)) % 11
        
            # controlecijfer omzetten naar stringvoorstelling
            return 'X' if controle == 10 else str(controle)

        if not self.isGeldig() or str(self.code)[:3] == '979':
            return None
        else:
            code = str(self.code)[3:-1]
            controle = controlecijfer(code)
            return '{}-{}-{}'.format(
                code[:self.lengte], 
                code[self.lengte:], 
                controle
            )
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()