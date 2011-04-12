import random

t = """
<html>
   <head>
   </head>
   <body style='font-size: 250px;'>
   %(content)s
   </body>
</html>
"""

f = open('/usr/share/dict/spanish')

def rand_word():
    return random.choice(f.readlines(512))

def rand_int():
    return str(random.randint(1,100))

def application(environ, start_response): 
    path = environ['PATH_INFO']

    response = ""

    if path == "/int":
        response = rand_int()
    elif path == "/word":
        response = rand_word()
    else:
        response = "La ruta %s no existe" % path
    
    response = t%{'content': response}

    start_response(
          "200 OK",
          [('Content-Type', 'text/html'),
           ('Content-Length', str(len(response)))]
          )
    return [response]

from wsgiref.simple_server import make_server

daemon = make_server('127.0.0.1', 8000, application)

daemon.serve_forever()
