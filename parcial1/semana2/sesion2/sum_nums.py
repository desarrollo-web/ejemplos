from wsgiref.simple_server import make_server
from cgi import parse_qs

def sum_nums(text):
  return sum([int(e) for e in text if e.isdigit()])

def app(environ, start_response):
  get = parse_qs(environ['QUERY_STRING'])
  text = ''.join([e[0] for e in get.values()])
  body="""<html>
            <body style='font-size: 250px;'>
            %s
            <body>
         </html>"""%sum_nums(text)
  start_response(
          "200 OK",
          [('Content-Type', 'text/html'),
           ('Content-Length', str(len(body)))]
          )
  return [body]

daemon = make_server("localhost", 8000, app)

daemon.serve_forever()
  
