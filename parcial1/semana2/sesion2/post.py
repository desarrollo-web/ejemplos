import random
from cgi import parse_qs
t = """
<!DOCTYPE html>
<html>
   <body style='font-size: 75px;'>
   <form method="post">
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

    try:
        body_size = int(environ.get('CONTENT_LENGTH', 0))  
    except ValueError:
        body_size = 0

    request_body = environ['wsgi.input'].read(body_size)

    POST= parse_qs(request_body)

    name = POST.get('name', 'No se ha ingresado')
    age  = POST.get('age', 'No se ha ingresado')

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
