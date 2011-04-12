#encoding=utf-8

"""
Una aplicación sencilla que se apega al protocolo WSGI
"""

def application(environ, #un diccionario llenado por WSGI
        start_response):  #una función que dice cómo responder
  text = ""
  for k,v in environ.items():
      text += "%s: %s\n"%(k,v)

  start_response(
          #status
          "200 OK",
          #headers
          [('Content-Type', 'text/plain'),
           ('Content-Length', str(len(text)))]
          )
  return [text]

from wsgiref.simple_server import make_server

daemon = make_server('127.0.0.1', 8000, application)

daemon.serve_forever()

