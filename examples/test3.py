def f(x):
    return g(x)


def g(x):
    x + 1
    ~x
    print(x < x > x)
    return x


print(f(5) + 1)
