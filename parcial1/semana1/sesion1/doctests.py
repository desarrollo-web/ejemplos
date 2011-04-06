#encoding=utf-8
"""
Ejemplo de uso de doctests:
Este es un comentario multilínea, arriba hay un comentario de una sola línea
(que, de casualidad, declara que este es un archivo unicode)

Un doctest es una simulación de una sesión del intérprete
"""

def types(l):
    """
    Devuelve una lista con los tipos de los elementos de la original
    >>> types([1, 2.0, 3+4j, "str", 'str', (1,2,3)])
    [<type 'int'>, <type 'float'>, <type 'complex'>, <type 'str'>, <type 'str'>, <type 'tuple'>]
    >>> types([ [4,5,6], {'a':1, (2,3):"dos"}, lambda x: x, True, None, types])
    [<type 'list'>, <type 'dict'>, <type 'function'>, <type 'bool'>, <type 'NoneType'>, <type 'function'>]
    """
    #equivale a return map(type, l)
    return [type(e) for e in l]


#Truco para que las pruebas se ejecuten SÓLO si el módulo es corrido directamente
if __name__ == "__main__":
    import doctest
    doctest.testmod()
