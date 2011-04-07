#encoding=utf-8

"""
Ejemplos de funciones de orden superior
"""


def quicksort(l, key=lambda x:x):
    """
    Ordenamiento con quicksort

    el parámetro opcional ``key`` es una función
    que se le aplicará a cada elemento, para encontrar
    el criterio de ordenamiento
    >>> quicksort([4,3,2,1,0])
    [0, 1, 2, 3, 4]
    >>> quicksort([[3,2,1], [2,3], [1]], key= lambda l: len(l) )
    [[1], [2, 3], [3, 2, 1]]
    >>> quicksort([[3,2,1], [2,3], [1]], key=len)
    [[1], [2, 3], [3, 2, 1]]
    >>> quicksort([{'age': 10, 'nom': 'lulu'},{'age': 1, 'nom': 'cthulhu', 'plus': 'que'},{'age':666}], key=lambda e: e['age'])
    [{'nom': 'cthulhu', 'age': 1, 'plus': 'que'}, {'nom': 'lulu', 'age': 10}, {'age': 666}]
    """

    if l==[]:
        return []
    else:
        head, tail = l[0], l[1:]
        return quicksort([e for e in tail if key(e) < key(head)], key)\
               +[head]+\
               quicksort([e for e in tail if key(e) >= key(head)], key)


def compose_3(f,g,h):
    """
    Composición de funciones: devuelve una función que aplica las tres originales, en cadena,
    a un argumento.
    Nótese que, en la segunda prueba, estamos llamando inmediatamente a la función que se nos
    retorna.

    >>> f = compose_3(str.split, str.title, lambda s: s.replace("_", " "))
    >>> f("hola_mundo")
    ['Hola', 'Mundo']
    >>> compose_3(str.split, str.title, lambda s: s.replace("_", " "))("hola_mundo")
    ['Hola', 'Mundo']
    """
    def composed(x):
        return f(g(h(x)))
    return composed

def compose(*funs):
    """
    Composición en el caso general: aplica todas las funciones en cadena
    desde la última a la primera

    ¿Qué hace la función predefinida ``reduce``?

    >>> import operator as op
    >>> compose(op.invert, op.neg)(666)
    665
    >>> compose(lambda x: x << 2, lambda x: x % 2, lambda x: x**2)(365)
    4
    """
    return lambda x: reduce(lambda acum, f: f(acum), funs[::-1], x)


def partial(f, *preloaded_args, **preloaded_kwargs):
    """
    Aplicación parcial de funciones

    retorna una función que acepta los argumentos que le "faltan" a la original
    >>> sum3 = lambda x,y,z: x+y+z
    >>> sum3(1,2,3)
    6
    >>> sum3_with_1 = partial(sum3, 1)
    >>> sum3_with_1(2,3)
    6
    >>> sorted("mundo hola algo".split(), key=len)
    ['hola', 'algo', 'mundo']
    >>> sort_by_len = partial(sorted, key=len)
    >>> sort_by_len("mundo hola algo".split())
    ['hola', 'algo', 'mundo']
    """
    
    def preloaded(*args, **kwargs):
        #¿Qué hace la función update de la clase dict?
        kwargs.update(**preloaded_kwargs)
        return f(*(preloaded_args+args), **kwargs)

    return preloaded

def flip(f):
    """
    Función que envía sus parámetros al revés a la original

    >>> import operator as op
    >>> op.lshift(8,2)
    32
    >>> shiftl = flip(op.lshift)
    >>> shiftl(8,2)
    512
    """

    def inverted(*args):
        return f(*(args[::-1]))

    return inverted

if __name__ == "__main__":
    import doctest
    doctest.testmod()
