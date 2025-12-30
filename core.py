from wsgiref.simple_server import make_server
from wsgi_dto import Request
from wsgiref import handlers, util, headers, types
import io

HELLO_WORLD = b"Hello, World!"

def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [("Content-type", 'text/plain')]
    start_response(status, response_headers)
    return[HELLO_WORLD]


class AppClass:
    """São basicamente o mesmo output, mas agora, com uma classe"""
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response
        self.counter = 1

    def __iter__(self):
        status = '200 OK'
        response_headers = [("Content-type", 'text/plain; charset="utf-8')]
        self.start(status, response_headers)
        request = Request(self.environ)
        yield HELLO_WORLD

app = AppClass
with make_server('', 8000, app) as httpd:
    print("Serving on port 8000")
    httpd.serve_forever()
