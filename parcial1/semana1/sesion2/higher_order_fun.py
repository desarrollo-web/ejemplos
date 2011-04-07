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



if __name__ == "__main__":
    import doctest
    doctest.testmod()
