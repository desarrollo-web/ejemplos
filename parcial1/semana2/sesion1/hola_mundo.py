#encoding=utf-8

"""
Una aplicación sencilla que se apega al protocolo WSGI
"""

def application(environ, start_response):
  text = 'Hola Mundo!'
  start_response(
          #status
          "200 OK",
          #headers
          [('Content-Type', 'text/plain'),
           ('Content-Length', str(len(text)))]
          )
  return [text]

from paste.httpserver import serve
serve(application)
