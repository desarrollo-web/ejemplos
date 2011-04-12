from webob import Request, Response

def echo(environ, start_response):
    req = Request(environ)
    res = Response(content_type="text/plain")
    res.body = "%s %s\n" % (req.method, req.path)
    for header, val in req.headers.items():
        res.body += "%s: %s\n" % (header, val)

    return res(environ, start_response)


from paste.httpserver import serve
serve(echo)
