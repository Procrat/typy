'''
Created on Feb 17, 2015

@author: david
'''
# eerste ISBN-10 code inlezen
code = input()

# opeenvolgende ISBN-10 codes inlezen totdat een regel wordt ingelezen die enkel
# het woord stop bevat
while code != 'stop':
    
    # controlecijfer berekenen
    controlecijfer = int(code[0])
    for i in range(2, 10):
        controlecijfer += i * int(code[i - 1])
    controlecijfer %= 11

    # controlecijfer uitlezen dat gebruikt wordt in ISBN-10 code    
    x10 = code[9]
    
    # nagaan of berekende controlecijfer gelijk is aan gebruikte controlecijfer
    if (controlecijfer == 10 and x10 == 'X') or x10 == str(controlecijfer):
        print('OK')
    else:
        print('FOUT')
    
    # volgende ISBN-10 code inlezen
    code = input()