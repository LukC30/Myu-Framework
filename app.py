def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    start_response(status, headers)
    print(str(environ))
    return [b'Ola mundo! finalmente uma aplicacao WSGI']