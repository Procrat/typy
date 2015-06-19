def f(x):
    return g(x)


def g(x):
    x + 1
    ~x
    return x


print(f(5) + 6)
f(5).non_existent_method()
