#encoding=utf-8
from Cookie import SimpleCookie
from cgi import parse_qs
from uuid import uuid1

base = """
<!DOCTYPE html>
<html>
   <head>
    <meta charset="utf-8"/>
   </head>
   <body style='font-size: 75px;'>
   %(contenido)s
   <a href="/">Cambiar cookie</a>
   <a href="/somewhere">Ir a cualquier lado</a>
   </body>
</html>
"""

form ="""
   <form method="get" action="set">
    <input type="text" name="name" placeholder="Nombre" style="width:500px;height:100px;font-size:75px"/>
    <input type="submit" />
   </form>
"""

import shelve
store = shelve.open('sesiones.db')

def _agregar(val):
    pk = uuid1().hex
    store[pk] = val
    return pk

store.add = _agregar 

def application(environ, start_response): 

    GET = parse_qs(environ['QUERY_STRING'])
    path = environ['PATH_INFO']
    cookies = SimpleCookie(environ.get('HTTP_COOKIE', ''))
    headers = {'Content-Type': 'text/html'}

    if path == '/':
        response = base%{'contenido': form}
    elif path == '/set':
        cookies['sessionId'] = store.add(GET.get('name', ['NULL McNULL',])[0])
        response = base%{'contenido': '<div style="background-color:green;color:white">Cookie establecida</div>'}
        headers.update({'Set-Cookie': cookies['sessionId'].OutputString()})
    else:
        cookie = cookies.get('sessionId',None)
        name = cookie and store.get(cookie.value, None) or None
        response = base%{'contenido': "<p>El valor de la sesión es: %s</p>"%name if name else 'Ninguno'}
    
    headers.update({'Content-Length': str(len(response))})

    start_response(
          "200 OK",
          headers.items()
          )
    return [response]

from wsgiref.simple_server import make_server

daemon = make_server('127.0.0.1', 8000, application)

daemon.serve_forever()
