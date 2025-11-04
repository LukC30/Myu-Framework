from wsgiref.simple_server import make_server
from miniframe import MiniFrame

app = MiniFrame(title="Minha APIIII", description="CACHORRO")
"""
Rotas do nosso miniframe
"""
@app.route('/')
def read_route():
    return "<h1>Pagina Inicial</h1><p>Bem-vindo ao MeuSiteDinamico!</p>"

@app.route("/sobre")
def sobre():
    """Esta é a view para a página 'sobre'."""
    return "<h1>Sobre Nos</h1><p>Este site foi feito com o MiniFrame!</p>"


httpd = make_server('localhost', 8501, app)

print(f"Servidor funcionando no http://localhost:8501/")
for path, func in app._routes.items():
    print(f"- Caminho disponivel: {path} -> {func.__name__}()")

httpd.serve_forever()

