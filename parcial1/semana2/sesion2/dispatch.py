#encoding=utf-8

"""
Una idea de cómo haríamos un framework
"""

from webob import Request
import random
class Framework:
    def __init__(self, controllers):
        self.controllers = controllers

    def __call__(self, environ, start_response):
        """
        Sobrecarga del operador paréntesis, ahora esta clase
        se comporta como una de las funciones que WSGI espera
        """

        #Buscamos alguien que se pueda hacer cargo de esta ruta
        handler = self.controllers.get(environ['PATH_INFO'],
                                        lambda *args: '')

        #La única dependencia externa: algo que haga el parsing de
        #la request por nosotros
        response = handler(Request(environ))

        start_response(
              "200 OK" if response else "404 NOT FOUND",
              [('Content-Type', 'text/html'),
               ('Content-Length', str(len(response)))]
              )
        return [response]

    def serve(self):
        from wsgiref.simple_server import make_server
        daemon = make_server('127.0.0.1', 8000, self)
        daemon.serve_forever()


def rand_word(request):
    offset = request.GET.get('pool', 100)
    size = request.GET.get('size', 5)
    f = open('/usr/share/dict/words')
    return ' '.join(random.sample(f.readlines(offset), size))

def rand_int(request):
    start, stop, n = request.GET.get('start',0), request.GET.get('stop',100), request.GET.get('n',5)
    return '\n'.join([str(random.randrange(start, stop)) for i in range(n)])

Framework({
    '/int': rand_int,
    '/word': rand_word
    }).serve()
