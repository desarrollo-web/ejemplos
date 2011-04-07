#encoding=utf-8

class Point:
    """
    Representa puntos en planos 

    >>> Point()
    (0, 0)
    >>> Point(y=6)
    (0, 6)
    >>> a = Point(1,1)
    >>> a.distance(Point())
    1.4142135623730951
    >>> Point(1,1) + Point(2,2)
    (3, 3)
    """

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self, o):
        o = o if o else Point()
        return ((o.x - self.x)**2 + (o.y - self.y)**2)**0.5

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
    
    __repr__ = __str__

class CountDict(dict):
    """
    Un diccionario para contar cosas

    >>> x =  CountDict()
    >>> x.put_or_inc('a')
    >>> x
    {'a': 1}
    >>> x.put_or_inc('a')
    >>> x
    {'a': 2}
    """

    def put_or_inc(self, k):
        self.update({k: self.get(k,0)+1})

class Struct(dict):
    """
    Un diccionario que se comporta como clase (¿o al revés?)
    >>> s = Struct()
    >>> s
    {}
    >>> s.hola = "mundo"
    >>> s
    {'hola': 'mundo'}
    >>> s.hola
    'mundo'
    >>> s['hola']
    'mundo'
    """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self



class Vector(list):
    """
    Representa vectores inmutables, hereda de tuple
    
    Muestra de herencia y sobrecarga de operadores

    >>> Vector(1,2,3)
    [1, 2, 3]
    >>> a = Vector(1,1,1)
    >>> b = Vector(2,2,2)
    >>> a == b
    False
    >>> Vector(1,1,1) + Vector(3,3,3)
    [4, 4, 4]
    >>> Vector(3,3,3) - Vector(2,2,2)
    [1, 1, 1]
    >>> 4 * Vector(2,2,2)
    [8, 8, 8]
    >>> Vector(1,1,1) * Vector(2,2,2)
    6
    """
    
    def __init__(self, *elems):
        #Llamada al constructor de la super-clase
        list.__init__(self, elems)
    
    def __add__(self, o):
        """
        Suma de vectores
        """

        return Vector(*[a+b for a,b in zip(self, o)])

    def __sub__(self, o):
        """
        Resta de vectores
        """

        return Vector(*[a-b for a,b in zip(self, o)])
    
    def __mul__(self, o):
        """
        Producto punto
        """
        return sum([a*b for a,b in zip(self, o)])

    def __rmul__(self, k):
        """
        Producto escalar
        """

        return Vector(*[k*e for e in self])

class Tree:
    """
    Representa un árbol

    >>> tree = Tree('c', Tree('b', Tree('a'))) 
    >>> for leaf in tree:
    ...     print leaf
    ...
    a
    b
    c
    >>> 'y' in Tree('x', Tree('a'), Tree('z', Tree('a')))
    True
    >>> 'm' in Tree('x', Tree('a'), Tree('z', Tree('a')))
    False 
    """

    def __init__(self, datum, right=None, left=None):
        self.datum = datum
        self.right = right
        self.left  = left

    def __iter__(self):

        if self.right:
            for e in self.right:
                yield e

        yield self.datum

        if self.left:
            for e in self.left:
                yield e

    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

