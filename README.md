<!-- Cabeçalho Centralizado -->
<div align="center">
  <!-- <a href="https://github.com/seu-usuario/Myu-Framework">
    <img src="https://raw.githubusercontent.com/MicaelliMedeiros/micaellimedeiros/master/image/computer-illustration.png" alt="Logo" width="100">
  </a> -->

  <h3 align="center">Myu-Framework</h3>

  <p align="center">
    Um micro-framework web em Python, construído do zero para fins educacionais.
    <br />
    Focado em simplicidade e em demonstrar os conceitos fundamentais do padrão WSGI.
    <br />
    <br />
    <a href="#-como-usar"><strong>Ver Exemplo de Uso »</strong></a>
  </p>
</div>

<!-- Badges (Escudos) -->
<div align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/status-em--desenvolvimento-yellow" alt="Status">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</div>

---

## 📋 Índice

1. [🔭 Sobre o Projeto](#-sobre-o-projeto)
   - [Funcionalidades](#funcionalidades)
2. [🚀 Começando](#-começando)
   - [Pré-requisitos](#pré-requisitos)
   - [Instalação](#instalação)
3. [🎈 Como Usar](#-como-usar)
4. [🤝 Contribuição](#-contribuição)
5. [📝 Licença](#-licença)
6. [📧 Contato](#-contato)

---

## 🔭 Sobre o Projeto

<p>
  O <strong>Myu-Framework</strong> nasceu como um projeto de estudo com o objetivo de desmistificar o funcionamento de frameworks web como Flask e Django. Ele implementa a especificação <a href="https://wsgi.readthedocs.io/">WSGI</a> (Web Server Gateway Interface) do zero, oferecendo uma visão clara de como as requisições HTTP são recebidas, processadas e respondidas em uma aplicação Python.
</p>

<p>
  É a ferramenta perfeita para quem deseja entender o que acontece "por baixo dos panos" no desenvolvimento web com Python.
</p>

### Funcionalidades

----
*   ✅ **Roteamento com Decorators:** Defina rotas de forma limpa e declarativa, similar aos frameworks modernos.
*   ✅ **Parâmetros de URL Dinâmicos:** Capture valores diretamente da URL (ex: `/user/{id}`).
*   ✅ **Objetos Request e Response:** Classes simples para manipular dados da requisição (JSON, formulários) e construir respostas.
*   ✅ **Renderização de Templates:** Um sistema básico para renderizar arquivos HTML e injetar contexto.
*   ✅ **Zero Dependências Externas:** Construído inteiramente com a biblioteca padrão do Python para máximo aprendizado.

---

## 🚀 Começando

Siga estas etapas para ter o projeto em execução na sua máquina local.

### Pré-requisitos

Você precisa ter o Python 3.8 ou superior instalado.

### Instalação

Como o projeto não possui dependências externas, basta clonar o repositório:

```sh
git clone https://github.com/seu-usuario/Myu-Framework.git
cd Myu-Framework
```

---

## 🎈 Como Usar

A melhor forma de entender o Myu-Framework é vendo-o em ação. Crie um arquivo `app.py` na raiz do projeto com o seguinte conteúdo:

```python
# app.py
from wsgiref.simple_server import make_server
from src.myuframe import MyuFrame, render_template
from src.wsgi_dto import Response

# 1. Crie uma instância do framework
app = MyuFrame(title="Meu App", description="Um app de exemplo")

# 2. Crie um template em /src/template/index.html
#    <h1>Olá, {{ nome }}!</h1>

# 3. Defina as rotas com decorators
@app.route("/")
def home(request):
    # Renderiza um template passando um contexto
    return render_template("index.html", context={"nome": "Mundo"})

@app.route("/user/{name}")
def user_profile(request, name):
    # Usa parâmetros dinâmicos da URL
    return Response(f"<h1>Página de {name.capitalize()}</h1>")

@app.route("/login", methods=["POST"])
def login(request):
    # Processa dados de formulário ou JSON
    data = request.form or request.json
    username = data.get("username", "visitante")
    return Response(f"<h3>Bem-vindo, {username}!</h3>")

# 4. Execute com um servidor WSGI
if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print("🚀 Servidor rodando na porta 8000...")
        httpd.serve_forever()
```

Para rodar, execute no terminal:

```sh
python app.py
```

Agora você pode acessar as rotas no seu navegador:
*   `http://localhost:8000/`
*   `http://localhost:8000/user/ana`

---

## 🤝 Contribuição

Contribuições tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito bem-vinda**.

1.  Faça um Fork do projeto
2.  Crie uma Branch para sua Feature (`git checkout -b feature/FeatureIncrivel`)
3.  Adicione suas mudanças (`git add .`)
4.  Comite suas mudanças (`git commit -m 'Adicionando uma FeatureIncrivel'`)
5.  Faça o Push da Branch (`git push origin feature/FeatureIncrivel`)
6.  Abra um Pull Request

---

## 📝 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---

## 📧 Contato

[Seu Nome] - [@seu_twitter] - [seu_email@exemplo.com]

Link do Projeto: https://github.com/seu-usuario/Myu-Framework

