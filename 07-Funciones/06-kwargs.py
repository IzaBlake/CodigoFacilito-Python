def promedio(*args):  # Tupla
    return sum(args) / len(args)


def usuarios(**kwargs):  # Dict
    print(kwargs)
    print(type(kwargs))


def combinacion(p1, p2, *args, p5=999, **kwargs):
    print(args)
    print(kwargs)


combinacion(1, 2, 3, 4, 5, p5=400, cody=True, curso='Python')
