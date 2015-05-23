def isISBN(code, isbn13 = True):
    if isbn13:
        code=str(code)
        for i in range(0,12):
            if code[i] not in "0123456789":
                return False
        controle=int((10-(int(code[0])
                            +int(code[2])
                            +int(code[4])
                            +int(code[6])
                            +int(code[8])
                            +int(code[10])
                            +3*(int(code[1])
                                +int(code[3])
                                +int(code[5])
                                +int(code[7])
                                +int(code[9])
                                +int(code[11])))%10)%10)
        if controle == 10:
            controle = "X"
            
        return str(controle) == code[12]
    else:
        code=str(code)
        for i in range(0,9):
            if code[i] not in "0123456789":
                return False
        
            controle=int((int(code[0])
                          +2*int(code[1])
                          +3*int(code[2])
                          +4*int(code[3])
                          +5*int(code[4])
                          +6*int(code[5])
                          +7*int(code[6])
                          +8*int(code[7])
                          +9*int(code[8]))%11)
            if controle == 10:
                controle = "X"
    
            return str(controle) == code[9]
        
def zijnISBN(codes, isbn13=None):
    
    returnValue=[]
    for code in codes:
        if isbn13 == None:
            if not isinstance(code,str):
                returnValue.append(False)
            elif len(str(code)) == 13:
                returnValue.append(isISBN(code, True))
            elif len(str(code)) == 10:
                returnValue.append(isISBN(code, False))
            else:
                returnValue.append(False)
        elif isbn13:
            if not isinstance(code,str):
                returnValue.append(False)
            elif len(str(code)) == 13:
                returnValue.append(isISBN(code, True))
            else:
                returnValue.append(False)
        else:
            if not isinstance(code,str):
                returnValue.append(False)
            elif len(str(code)) == 10:
                returnValue.append(isISBN(code, False))
            else:
                returnValue.append(False)
    return returnValue

print(zijnISBN(['0012345678', '0012345679', '9971502100', '080442957X', 5, True, 'The Practice of Computing Using Python', '9789027439642', '5486948320146']))
