#encoding=utf-8

"""
Ejemplos varios de operaciones sobre listas
¿Qué hace la función eval?
"""

def say_and_eval(exp_list):
    """
    Agarra una lista de expresiones de python, las muestra y luego las ejecuta
    """
    for exp in exp_list:
        print ">>> %s\n => %s" %(exp, eval(exp))


lista = range(10)
n = 16
say_and_eval([
    "lista",
    #List slicing
    "lista[0]",
    "lista[-1]",
    "lista[2:6]",
    "lista[2:6:2]",
    "lista[2:]",
    "lista[:6]",
    "lista[::-1]",
    "lista[6:2:-1]",
    "lista[:]",
    #algunas funciones predefinidas
    "len([1,2,3,4])",
    "max([4,3,1,5])",
    #operadores sobrecargados
    "'hola'*10",
    "[1,2]+[3,4]",
    #List comprehensions
    "[e**0.5 for e in  range(4)]",
    #el equivalente con funciones de orden superior:
    "map(lambda e: e**0.5, range(4))",
    "[e for e in range(10) if not e % 2]",
    #con funciones de orden superior:
    "filter(lambda e: not e%2, range(10))",
    #El problema de las ternas pitagóricas: http://es.wikipedia.org/wiki/Terna_pitag%C3%B3rica
    "[(a,b,c) for a in range(1,n) for b in range(1,n) for c in range(1,n) if a+b+c <= n and a*a+b*b==c*c]",
])
