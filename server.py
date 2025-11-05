from wsgiref.simple_server import make_server
from miniframe import MiniFrame, Response

app = MiniFrame(title="Minha APIIII", description="CACHORRO")

#Rotas do nosso miniframe
@app.route("/")
def home(request):
    """
    View da Home.
    Assinatura: (request)
    """
    body = f"<h1>Pagina Inicial</h1>"
    body += f"<p>Acesse <a href='/user/123'>/user/123</a></p>"
    body += f"<p>Ou <a href='/user/ana'>/user/ana</a></p>"
    return Response(body)

@app.route("/sobre")
def sobre(request):
    """
    View da página Sobre.
    Assinatura: (request)
    """
    body = "<h1>Sobre Nos</h1><p>Este site foi feito com o MiniFrame!</p>"
    return Response(body)

@app.route('/sla/{user}')
def user(request, username):
    """
    View de usuário.
    Assinatura: (request, username)
    O 'username' vem da mágica do **kwargs no __call__!
    """
    body = f"<h1>Pagina do usuario: {username}</h1>"
    body += f"<p>Voce acessou o caminho: {request.path}</p>"
    body += f"<p>O framework extraiu <strong>'{username}'</strong> da URL para voce.</p>"
    body += f"<a href='/'>Voltar para a Home</a>"

    if username == 'adeeme':
        body += "<h2>Voce e um ADMIN!</h2>"

    return Response(body)

#Criacao do server
httpd = make_server('localhost', 8501, app)

print(f"Servidor funcionando no http://localhost:8501/")
print("Rotas dispponiveis")
for path, func in app._routes.items():
    print(f"- Caminho disponivel: {path} -> {func.__name__}()")

httpd.serve_forever()

