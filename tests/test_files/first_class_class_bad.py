def f(value):
    class X:
        class_attr = value
    return X


f(5).class_attr.non_attr
