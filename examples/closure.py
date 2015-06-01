def f():
    x = 5
    def g():
        x + 1
        return x
    return g


f()()


def g():
    x = 5
    def h():
        x.lolcatz
        return x
    return h


g()()
