import re
from pathlib import Path
from wsgi_dto import Response, Request

BASE_DIR = Path(__file__).parent
TEMPLATE_DIR = BASE_DIR / 'template'

def render_template(template, context):
    print(f'Renderizando template: {template}')

    template_path = TEMPLATE_DIR/template

    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            html_bruto = f.read()
        html = html_bruto
        for k, v in context.items():
            placeholder = f"{{{{ {k} }}}}"
            html = html.replace(placeholder, str(v))
        return Response(body=html, content_type='text/html')

    except FileNotFoundError:
        print(f"ERRO DE TEMPLATE: Arquivo '{template_path}' nao encontrado.")
        return Response(
            body=f"<h1>500 Erro Interno</h1><p>Template '{template}' nao foi encontrado.</p>",
            status_code=500
        )

    except Exception as e:
        print(f"ERRO DE TEMPLATE: {e}")
        return Response(f"<h1>500 Erro Interno</h1><p>{e}</p>", status_code=500)

class MyuFrame():

    def __init__(self, title, description):
        self.title = title
        self.description = description
        print(f"Miniframe criado na instancia: {self.title}")
        self._routes = []

    #Aqui fica a cargo de escrita e adição
    def route(self, path, methods=None):

        if not methods:
            methods = ["GET"]

        methods = [m.upper() for m in methods]

        param_names = re.findall(r"\{(\w+)\}", path)
        regex_path = re.sub(r"\{\w+\}", r"([^/]+)", path)
        regex_pattern = f"^{regex_path}$"
        regex_compile = re.compile(regex_pattern)

        print(f"Registrando rota: {path} -> {regex_pattern}")

        def decorator(handler_function):
            self._routes.append(
                (regex_compile, param_names, methods, handler_function)
            )
            return handler_function

        return decorator

    #Aqui fica a cargo de consulta
    def __call__(self, environ, start_response):

        request = Request(environ)
        print(f'\n__call__ rodou: Recebendo request para {request.path}')
        response = None
        path_matches_but_method_doesnt_exist = False

        for regex, param_names, http_methods, handler_function in self._routes:
            match = regex.match(request.path)

            if not match:
                continue

            if request.method not in http_methods:
                path_matches_but_method_doesnt_exist = True
                continue

            print(f"Rota encontrada. Padrão utilizado: {regex.pattern}")

            values = match.groups()
            kwargs = dict(zip(param_names, values))

            try:
                response = handler_function(request, **kwargs)
            except Exception as e:
                print(f"Erro na view: {e}")
                response = Response(f"<h1>500 Erro Interno</h1><p>{e}</p>", status_code=500)
            break

        if response is None:
            if path_matches_but_method_doesnt_exist:
                print(f"Erro: Rota '{request.path}' encontrada, mas metodo não existe ")
                response = Response(
                    body=f"<h1>4Não 405 Metodo Nao Permitido</h1><p>O metodo '{request.method}' nao e permitido para a rota '{request.path}'.</p>",
                    status_code=405
                )
            else:
                print(f'erro: rota "{request.path}" nao encontrada')
                response = Response(
                    body=f"<h1>Pagina não encontrada</h1><p>a rota {request.path} não existe</p>",
                    status_code=404
                )

        print(f"Enviando resposta: {response.status_string}")
        start_response(response.status_string, response.headers)
        return [response.body]