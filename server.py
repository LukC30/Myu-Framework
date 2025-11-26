from wsgiref.simple_server import make_server
from myuframe import MyuFrame, render_template
from wsgi_dto import Response

import json

app = MyuFrame(title="Minha APIIII", description="CACHORRO")

#Rotas do nosso miniframe
@app.route("/", methods=["GET"])
def home(request):
    context = {
        'title' : "eu sou mto macaco pprt",
        'main_title': "Vamos juntos"
    }
    return render_template('home.html', context)

@app.route("/user/{username}", methods=["GET"])
def show_user(request, username):
    contexto = {
        'nome_do_usuario': username,
        'caminho_da_url': request.path
    }
    return render_template("user_profile.html", contexto)

@app.route('/api/user', methods=["POST"])
def create_user(request):
    print(f'Criando usuario')

    data = request.json
    print(request, data)
    if not data:
        response_data = {'error': 'Nenhum dado JSON válido foi enviado.'}
        return Response(
            body=json.dumps(response_data),
            status_code=400,
            content_type="application/json"
        )
    
    login = data.get("user")
    passw = data.get("password")
    if not login or not passw:
        response_data = {'error': 'Não sei onde ta caindo'}
        return Response(
            body=json.dumps(response_data),
            status_code=400,
            content_type="application/json"
        )
    final_data = {
        'status' : 'success',
        'message' : 'request recebida com sucesso',
        'user' : {
            'login' : login,
            'password' : 'segredo shiiiiiii'
        }
    }
    return Response(body=json.dumps(final_data, indent=2), status_code=201 ,content_type='application/json')

#Criacao do server
httpd = make_server('localhost', 8501, app)

print(f"Servidor funcionando no http://localhost:8501/")
print("Rotas dispponiveis:")

for regex, params, methods, func in app._routes:
    print(f"- {regex.pattern} (Params: {params}, Methods: {methods}) -> {func.__name__}")

httpd.serve_forever()

