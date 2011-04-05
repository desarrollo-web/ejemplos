#encoding=utf-8

def same_fringe(l1, l2):
    """
    Revisa si dos listas tienen las mismas "hojas"
    en el mismo orden

    >>> same_fringe([1, [2,3], [[4,5,6]]], [1, 2, 3, [4,5], 6])
    True
    >>> same_fringe([1,2,3], [[3,2], 1])
    False
    """

def sort_by_freq(l):
    """
    Ordena una lista de iterables por la frecuencia de las longitudes de éstas

    >>> sort_by_freq([(a, b, c) (d, e) (f, g, h) (d, e) (i, j, k, l) (m, n) (o)])
    [(i, j, k, l) (o) (a, b, c) (f, g, h) (d, e) (d, e) (m, n)]
    >>> sort_by_freq(["abc", "de", "fgh", "de", "ijkl", "mn", "o"])
    ["ijkl","o","abc","fgh","de","de","mn"]
    """

def histogram(text):
    """
    Imprime un histograma de frecuencias para las palabras de un texto
    (Podría ser un archivo)

    >>> histogram("Hola mundo; ADIOS MUNDO")
    Palabra    Frecuencia
    =======    ==========
    hola       *
    mundo      **
    adios      *
    """

def eval_rpn(exp):
    """
    Evalúa una expresión en notación polaca inversa

    >>> eval_rpn("5 1 2 + 4 * 3 - +")
    14
    """


#Para que sólo se ejecute cuando se ejecuta directamente 
#Para ver las pruebas, usar:
#python ejercicios.py -v
if __name__ == "__main__":
    import doctest
    doctest.testmod()
