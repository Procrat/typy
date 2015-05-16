class A:
    bestaand_attr = 3

    def bestaande_functie():
        pass

    def bestaande_methode(self):
        pass


def f(x):
    x.bestaande_methode()
    x.bestaande_functie()  # Not correctly called; should fail
    return x.niet_bestaande_functie()


A.bestaande_functie()
f(A())
