from wsgiref.simple_server import make_server
from myuframe import MyuFrame, render_template
from wsgi_dto import Response

app = MyuFrame(title="Minha APIIII", description="CACHORRO")

#Rotas do nosso miniframe
@app.route("/", methods=["GET"])
def home(request):
    context = {
        'title' : "MACACO",
        'main_title': "Vai se foderf"
    }
    return render_template('home.html', context)

@app.route("/user/{username}", methods=["GET"])
def show_user(request, username):
    contexto = {
        'nome_do_usuario': username,
        'caminho_da_url': request.path
    }
    return render_template("user_profile.html", contexto)

@app.route('/login', methods=["GET"])
def user(request):

    body = """
            <h1>Formulario de Login</h1>
            <form action="/login" method="POST">
                <label for="user">Usuario:</label>
                <input type="text" id="user" name="username">
                <br>
                <label for="pass">Senha:</label>
                <input type="password" id="pass" name="password">
                <br>
                <input type="submit" value="Entrar">
            </form>
        """
    return Response(body)

@app.route('/login', methods=['POST'])
def handle_login_submit(request):

    print("Executando handle_login_submit (POST)")

    username = request.form.get("username", "N/A")
    password = request.form.get("password", 'N/A')

    body = f"<h1>Login Recebido!</h1>"
    body += f"<p>Ola, <strong>{username}</strong>!</p>"

    if username == 'admin' and password == '123':
        body += "<h2>Voce e um ADMIN! Login com sucesso!</h2>"
    else:
        body += "<h2>Usuario ou senha invalidos.</h2>"

    body += f"<p>(O que recebemos: username={username}, password={password})</p>"
    body += "<a href='/login'>Tentar novamente</a>"

    return Response(body)

#Criacao do server
httpd = make_server('localhost', 8501, app)

print(f"Servidor funcionando no http://localhost:8501/")
print("Rotas dispponiveis:")

for regex, params, methods, func in app._routes:
    print(f"- {regex.pattern} (Params: {params}, Methods: {methods}) -> {func.__name__}")

httpd.serve_forever()

