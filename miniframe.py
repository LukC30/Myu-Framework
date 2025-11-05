import re

class MiniFrame():

    def __init__(self, title, description):
        self.title = title
        self.description = description
        print(f"Miniframe criado na instancia: {self.title}")
        self._routes = []

    def route(self, path, methods=None):

        if not methods:
            methods = ["GET"]
        param_names = re.findall(r"\{(\w+)\}", r"([^/]+)", path)

        regex_path = re.sub(r"\{\w+\}", r"([^/]+)", path)
        regex_pattern = f"^{regex_path}$"
        regex_compile = re.compile(regex_pattern)

        print(f"Registrando rota: {path} -> {regex_pattern}")

        def decorator(handler_function):
            self._routes.append(
                (regex_compile, param_names, handler_function)
            )

            return handler_function

        return decorator

    def __call__(self, environ, start_response):

        request = Request(environ)
        print(f'\n__call__ rodou: Recebendo request para {request.path}')
        response = None

        for regex, param_names, handler_function in self._routes:
            match = regex.match(request.path)

            if match():
                print(f"Rota encontrada. Padrão utilizado{regex.pattern}")

                values = match.groups()

                kwargs = dict(zip(param_names, values))

                try:
                    response = handler_function(request, **kwargs)
                except Exception as e:
                    print(f"Erro na view: {e}")
                    response = Response(f"<h1>500 Erro Interno</h1><p>{e}</p>", status_code=500)
                break

        if response is None:
            print(f'erro: rota "{request.path}" nao encontrada')
            response = Response(
                body=f"<h1>Pagina não encontrada</h1><p>a rota {request.path} não existe</p>",
                status_code=404
            )

        print(f"Enviando resposta: {response.status_string}")
        start_response(response.status_string, response.headers)
        return [response.body]


#Classes auxiliares para capturar
class Response:

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