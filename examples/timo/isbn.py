
class ISBN13:

    def __init__(self, code, lengte=1):
        self.code = str(code)
        if 1 <= lengte <= 5:
            self.lengte = lengte

    def __str__(self):
        return self.code[:3]+"-"+self.code[3:3+self.lengte]+"-"+self.code[3+self.lengte:-1]+"-"+self.code[-1]

    def __repr__(self):
        return "ISBN13("+self.code+", "+str(self.lengte)+")"

    def isGeldig(self):
        if len(self.code) == 13:
            code = str(self.code)
            for i in range(0, 12):
                if code[i] not in "0123456789":
                    return False
            controle = int((10-(int(code[0])
                                + int(code[2])
                                + int(code[4])
                                + int(code[6])
                                + int(code[8])
                                + int(code[10])
                                + 3 * (int(code[1])
                                + int(code[3])
                                + int(code[5])
                                + int(code[7])
                                + int(code[9])
                                + int(code[11]))) % 10) % 10)
            return str(controle) == code[12]
        else:
            return False

    def alsISBN10(self):
        arr = str(self).split("-")
        if not self.isGeldig() or arr[0] != "978":
            return None
        nieuw = arr[1]+arr[2]
        controle = int((int(nieuw[0])
                        + 2 * int(nieuw[1])
                        + 3 * int(nieuw[2])
                        + 4 * int(nieuw[3])
                        + 5 * int(nieuw[4])
                        + 6 * int(nieuw[5])
                        + 7 * int(nieuw[6])
                        + 8 * int(nieuw[7])
                        + 9 * int(nieuw[8])) % 11)
        if controle == 10:
            controle = "X"
        return nieuw[0]+"-"+nieuw[1:]+"-"+str(controle)

code = ISBN13(9780136110675)
print(code.alsISBN10())


