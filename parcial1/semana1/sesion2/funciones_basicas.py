#encoding=utf-8
from __future__ import division

def bubblesort(x, ascending=True, make_copy=False):
    """
    Ordenamiento por burbuja estándar, que puede
    actuar sobre una lista o una copia de ésta

    En las pruebas, range(n)[::-1] es una lista invertida
    Sólo pongo casos demostrativos, hay más

    >>> bubblesort(range(5)[::-1])
    [0, 1, 2, 3, 4]
    >>> bubblesort(range(5), False)
    [4, 3, 2, 1, 0]
    >>> bubblesort(ascending=False, x=range(5))
    [4, 3, 2, 1, 0]
    >>> bubblesort(range(5)[::-1], make_copy=True)
    [0, 1, 2, 3, 4]
    """
    x = x[:] if make_copy else x

    for i in range(len(x)):
        for j in range(len(x)-1, i, -1):
            if ascending:
                if x[j-1] > x[j]:
                    x[j-1], x[j] = x[j], x[j-1]
            else:
                if x[j-1] < x[j]:
                    x[j-1], x[j] = x[j], x[j-1]
    return x

def avg(*items):
    """
    Muestra de argumentos posicionales variables

    recibe una cantidad cualquiera de argumentos y devuelve el promedio
    >>> avg(1,2,3,4)
    2.5
    >>> avg(*range(1,5))
    2.5
    >>> lista = [4,3,2,1]; avg(*lista)
    2.5
    """
    return sum(items)/len(items)

def print_hist(**tabla):
    """
    Muestra de argumentos con nombre variables

    recibe un diccionario e imprime un histograma de frecuencias
    >>> print_hist(hola=5, mundo=3)
    hola: *****
    mundo: ***
    >>> print_hist(**{'mundo': 2, 'hola': 3})
    mundo: **
    hola: ***
    >>> dicc={'llave': 4, 'otra':2}; print_hist(**dicc)
    llave: ****
    otra: **
    """
    
    for k,v in tabla.items():
        print k+": ", "*"*v

def combo(saludo, *args, **kwargs):
    """
    Combinación de parámetros posicionales, 
    posicionales variables y nombrados

    >>> combo("hola", do_print=True)
    hola
    >>> combo("mundo", 1,2,3,4, do_print=True)
    mundo
    1
    2
    3
    4
    """
    print saludo
    if 'do_print' in kwargs and kwargs['do_print']:
        for e in args:
            print e

def evil(x, l=[]):
    """
    ¡NUNCA pasar objetos mutables como parámetros por defecto!
    viven en el mismo ámbito que la función así que sobreviven 
    entre llamadas (no pertenecen a la función, sino a quien
    define la función)

    >>> evil(1)
    [1]
    >>> evil(2)
    [1, 2]
    >>> evil('c', ['a', 'b'])
    ['a', 'b', 'c']
    >>> evil(3)
    [1, 2, 3]
    """
    l.append(x)
    return l

if __name__ == "__main__":
    import doctest
    doctest.testmod()

