#encoding=utf-8

'''
Ejemplos de decoradores: más funciones que modifican a otras
esta vez usaremos el módulo de pruebas de unidad 
``unittest``: http://docs.python.org/library/unittest.html


Si necesitan más discusión: 
http://stackoverflow.com/questions/739654/understanding-python-decorators
'''

import json

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

@json_fun
def foobar(lista):

    assert isinstance(lista, list)
    
    #¿qué hace la función enumerate?
    return dict(enumerate(lista))


'''
También podemos tener fábricas de decoradores: funciones que retornan decoradores
'''

def pimp_string(with_effect="bold"):
    def decorator(f):
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)
            
            #¿qué hace esto?
            tag_with = lambda tag: "<%s>%s</%s>"%(tag, result, tag)

            if with_effect == 'bold':
                return tag_with('strong')
            elif with_effect == 'italic':
                return tag_with('em')
            elif with_effect == 'underline':
                return tag_with('u')
            else:
                return result

        return wrapper
    return decorator


@pimp_string()
def lorem_ipsum():
    return "Lorem ipsum dolor sic amet"


#Nada nos impide aplicar más de un decorador
@pimp_string(with_effect="italic")
@pimp_string(with_effect="underline")
def random_text():
    return """Hola, soy un string con
    varias lineas, nadie tiene problemas conmigo
    porque tengo triples comillas dobles"""

