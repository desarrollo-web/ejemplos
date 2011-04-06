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
        print "%s => %s" %(exp, eval(exp))


lista = range(10)

say_and_eval([
    "lista[0]",
    "lista[-1]",
    "lista[2:6]",
    "lista[2:6:2]",
    "lista[2:]",
    "lista[:6]",
    "lista[::-1]",
    "lista[6:2:-1]",
    "lista[:]",
])
