import random
from cgi import parse_qs
t = """
<!DOCTYPE html>
<html>
   <body style='font-size: 75px;'>
   <form method="get">
    <input type="text" name="name" placeholder="Nombre"/>
    <input type="text" name="age" placeholder="Edad"/>
    <input type="submit" />
   </form>

   <p>
    <dl>
        <dd>Nombre</dd>
        <dt>%(name)s</dt>
        <dd>Edad</dd>
        <dt>%(age)s</dt>
    </dl>
   </p>
   </body>
</html>
"""


def application(environ, start_response): 

    GET = parse_qs(environ['QUERY_STRING'])
    name = GET.get('name', 'No se ha ingresado')
    age  = GET.get('age', 'No se ha ingresado')

    response = t%{'name': name, 'age': age}

    start_response(
          "200 OK",
          [('Content-Type', 'text/html'),
           ('Content-Length', str(len(response)))]
          )
    return [response]

from wsgiref.simple_server import make_server

daemon = make_server('127.0.0.1', 8000, application)

daemon.serve_forever()
