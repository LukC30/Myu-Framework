#Classes auxiliares para capturar
import urllib.parse
import json

class Response:

    def __init__(self, body, status_code=200, content_type="text/html"):
        self.body = body.encode('utf-8')
        self.status_code = status_code
        self.content_type = content_type

        self.status_string = self._get_status_string(status_code)
        self.headers = [
            ('Content-Type', f'{content_type}; charset=utf-8'),
            ('Content-Length', str(len(self.body)))
        ]

    def _get_status_string(self, code):
        status = {
            200 : "200 OK",
            201 : "201 Created",
            302 : "302 Found",
            400 : "400 Bad Request",
            404 : "404 Not Found",
            405 : "405 Method Not Allowerd",
            500 : "500 Internal Server Error"
        }
        return status.get(code, '200 OK')


class Request:

    def __init__(self, environ: dict):
        self.environ = environ
        self.path = self.environ.get("PATH_INFO", '/')
        self.method = self.environ.get("REQUEST_METHOD", 'GET')

        self._form_data = {}
        self._json_data = None

        if self.method in ["POST", "PUT", "PATCH"]:
            try:
                length_str = environ.get("CONTENT_LENGTH", "0")
                content_length = int(length_str) if length_str else 0
                if content_length > 0:
                    body_stream = environ.get('wsgi.input')
                    body_bytes = body_stream.read(content_length)
                    body_string = body_bytes.decode("utf-8")

                    content_type = environ.get("CONTENT_TYPE", '').lower()
                    
                    print(body_string)
                    if 'application/x-www-form-urlencoded' in content_type:
                        self._form_data = urllib.parse.parse_qs(body_string)

                    elif 'application/json' in content_type:
                        self._json_data = json.loads(body_string)
                        print('passou por aqui')
                    
                    else:
                        print(f"Warning: Content-type {content_type} não suportado")

            except Exception as e:
                print(f"Erro ao ler o corpo do POST: {e}")
                self._form_data = {}
                self._json_data = None


    @property
    def form(self):
        return {k: v[0] for k, v in self._form_data.items()}

    @property
    def json(self):
        return self._json_data
    
    def __repr__(self):
        return f'<Request [{self.method}] {self.path}]>'