#encoding=utf-8

'''
Ejemplos de decoradores: más funciones que modifican a otras
esta vez usaremos el módulo de pruebas de unidad 
``unittest``: http://docs.python.org/library/unittest.html
'''

import json, pickle

def json_fun(f):
    def wrapper(json_string, *args, **kwargs):
        #modifico la entrada
        python_object = json.loads(json_string)

        #invoco a la función
        result = f(python_object, *args, **kwargs) 

        #modifico la salida
        return json.dumps(result)

    return wrapper

'''
A continuación vienen dos formas de agarrar una función y transformarla:
una es re-asignación, como en la función ``foo``

La otra es decoración, que es totalmente equivalente a la re-asignación
'''

def foo(mapa):
    
    #¿Qué hacen assert e isinstance?

    assert isinstance(mapa, dict)
    return dict(zip(mapa.values(), mapa.keys()))

foo = json_fun(foo)

@@@json_fun
def foobar(lista):

    assert isinstance(lista, list)
    #¿qué hace la función enumerate?
    return dict(enumerate(lista))


'''
También podemos tener fábricas de decoradores: funciones que retornan decoradores
'''

def serialize(format="json"):
    def decorator(f):
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            if format == 'json':
                return json.dumps(result)
            elif format == 'pickle':
                return pickle.dumps(result)
            else:
                throw Exception("Invalid format")
        return wrapper
    return decorator

@@@serialize()
def tage():
    from calendar import day_name
    return dict(zip("Montag Dienstag Mittwoche Donnerstag Freitag Samtag Suntag".split(), list(day_name)))

@@@serialize(format='pickle')
def mons():
    from calendar import month_name
    return dict(zip("Janvier Fevrier Mars Avril".split(), list(month_name)[1:5]))
    
