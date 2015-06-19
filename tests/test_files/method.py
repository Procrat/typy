class A:
    def bestaande_methode(self):
        pass


def f(x):
    return x.bestaande_methode()


f(A())
