class MiniFrame():
    def __init__(self, title, description):
        self.title = title
        self.description = description
        print(f"Miniframe criado na instancia: {self.title}")
        self._routes = {}

    def route(self, path):

        def decorator(handler_function):

            print(f"Registrando rota: {path} -> {handler_function.__name__}")
            self._routes[path] = handler_function

            return handler_function

        return decorator

    def __call__(self, environ, start_response):
        requested_path = environ.get('PATH_INFO', '/')
        print(f'\n__call__ rodou: Recebendo request para {requested_path}')

        handler = self._routes.get(requested_path)
        if handler:
            print(f"Rota encontrada, executando... {handler.__name__}")

            body_str = handler()
            status_code = '200 OK'
            headers = [('Content-Type', 'text/html; charset=utf-8')]
            start_response(status_code, headers)

            return [body_str.encode('utf-8')]
        print(f"Error: rota não encontrada para {requested_path}")
        status_code = '404 Not Found'
        headers = [('Content-Type', 'text/html; charset=utf-8')]
        start_response(status_code, headers)

        body_str = f"<h1>404 Pagina Nao Encontrada</h1><p>A rota '{requested_path}' nao existe no {self.title}.</p>"
        return [body_str.encode('utf-8')]

class Response:
    """

    """
    def __init__(self, body, status_code=200, content_type="text/html"):
        self.body = body.encode('utf-8')
        self.status_code = status_code
        self.content_type = content_type

        self.status_string = self._get_status_string(status_code)
        self.headers = [
            ('Content-Type', f'{content_type}; charset=utf-8'),
            ('Content-Lenght', str(len(self.body)))
        ]


    def _get_status_string(self, code):
        status = {
            200 : "200 OK",
            404 : "404 Not Found",
            302 : "302 Found"
        }
        return status.get(code, '200 OK')

class Request:
    def __init__(self, environ: dict):
        self.environ = environ
        self.path = self.environ.get("PATH_INFO", '/')
        self.method = self.environ.get("REQUEST_METHOD", 'GET')

    def __repr__(self):
        return f'<Request [{self.method}] {self.path}'