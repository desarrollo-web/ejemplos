#encoding=utf-8

"""
Una aplicación sencilla que se apega al protocolo WSGI
"""

def application(environ, #un diccionario llenado por WSGI
        start_response):  #una función que dice cómo responder
  text = 'Hola Mundo!\n'
  start_response(
          #status
          "200 OK",
          #headers
          [('Content-Type', 'text/plain'),
           ('Content-Length', str(len(text)))]
          )
  return [text]

class ReverseMiddleware:
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response):
        for data in self.wrapped_app(environ, start_response):
            return data[::-1]

from wsgiref.simple_server import make_server

daemon = make_server('127.0.0.1', 8000, ReverseMiddleware(application))

daemon.handle_request()

