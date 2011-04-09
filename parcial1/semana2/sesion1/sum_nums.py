from webob import Request, Response

def sum_nums(text):
  return sum([int(e) for e in text if e.isdigit()])

def app(environ, start_response):
  request = Request(environ)
  text = ''.join(request.GET.keys())
  response = Response(content_type='text/html',
          body="""<html>
                    <body style='font-size: 250px;'>
                    %s
                    <body>
                 </html>"""%sum_nums(text))
  return response(environ, start_response)

from paste.httpserver import serve
serve(app)

  
