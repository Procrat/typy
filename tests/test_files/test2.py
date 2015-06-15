class A:
    bestaand_attr = 3

    def bestaande_functie():
        pass

    def bestaande_methode(self):
        pass


def f(x):
    # x.bestaande_functie()  # Not correctly called
    # x.niet_bestaande_methode()
    return x.bestaande_methode()


A.bestaande_functie()
f(A())
