# Aula 2 - Introdução ao Django, URLs, Views e Templates

- Vamos começar retornando à pasta que criamos ontem para o nosso projeto. Conseguem lembrar do comando?

- Na pasta do nosso curso, vamos dar início ao projeto propriamente dito. A primeira coisa que precisamos é iniciar o Django Framework, que criará o esqueleto para a nossa aplicação

- Nosso comando será: `django-admin.exe startproject controlefinanceiro .`

- Você irá notar que algumas pastas foram criadas. Nós iremos observá-las depois.

- Agora execute: `cd controlefinanceiro` para acessar a pasta do projeto

- E vamos iniciar nosso servidor local com o comando: `python manage.py runserver`

- Se você conseguir acessar o endereço: http://127.0.0.1:8000/, parabéns, a configuração foi um sucesso!

# Estrutura de um projeto Django

- O Django trabalha com um padrão chamado MVT (Model-View-Template).

> **Model**: Responsável pelo gerenciamento de dados e interação com o banco de dados.

> **View**: Responsável pela lógica da aplicação, definindo o que pode ou não ser mostrado e para quem.

> **Template**: Responsável pela apresentação dos dados ao usuário. É aqui que ficarão nossos arquivos HTML.


Outras coisas importantes de se reparar são...

## manage.py
Script responsável por nos ajudar com a gestão do site.

## Pasta controlefinanceiro

### settings.py
Arquivo responsável por gerenciar as configurações do nosso projeto.

### urls.py
Arquivo no qual iremos configurar os endereços de acesso e páginas do nosso projeto

# Algumas configurações iniciais

- No arquivo `settings.py`, vamos definir a nossa linguagem como português brasileiro e o fuso-horário do Brasil substituindo os parâmetros a seguir:

```python
LANGUAGE_CODE = 'pt-BR`
TIME_ZONE = 'America/Sao_Paulo
```

- Lembrem de salvar as modificações!

# Criação do nosso primeiro app

- Para esta aula iremos criar um app com duas páginas: Uma página inicial e uma página "sobre" com a descrição do nosso projeto.

- Iniciamos com o comando `python manage.py startapp base` ("base" é o nome do app)

- Pode reparar que uma nova pasta para esse app foi criada! Agora vamos registrar esse app no arquivo `settings.py`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
]
```

# Primeiras configurações do nosso app de base

- Mude para a pasta da aplicação usando o comando `cd base`

- Crie o arquivo `urls.py`

- Dentro do arquivo escreva:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
]
```

- Agora vamos criar nossas views. No arquivo `views.py` na pasta `base` escreva:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')
```

- Agora conectamos esse app `base` as urls da nossa aplicação principal.

- No arquivo `urls.py` da pasta `controlefinanceiro` escreva:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
]
```

# Criando nossos primeiros templates

- Voltando para a pasta `base`, criaremos dentro dela uma pasta chamada `templates`.

- Essa pasta servirá para armazenarmos os templates em HTML das páginas que criaremos hoje.

- Dentro da pasta `templates` vamos criar mais uma pasta chamada `base` e dentro dela três arquivos, são eles:

> raiz.html

> index.html

> sobre.html

- No arquivo `raiz.html` cole o código a seguir:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Controle Financeiro</title>
</head>
<body>
    <nav>
        <a href="/">Início</a> |
        <a href="/sobre/">Sobre</a>
    </nav>
    <hr>
    {% block content %}
    {% endblock %}
</body>
</html>
```

- No arquivo `index.html` cole o código a seguir:

```html
{% extends "base/raiz.html" %}

{% block content %}
<h1>Bem-vindo ao Controle Financeiro Pessoal</h1>
<p>Gerencie suas receitas, despesas e investimentos de forma prática.</p>
{% endblock %}
```

- No arquivo `sobre.html` cole o código a seguir:

```html
{% extends 'base/raiz.html' %}

{% block title %}Sobre{% endblock %}

{% block content %}
<h1>Sobre o Projeto</h1>
<p>Este é um sistema de controle financeiro pessoal desenvolvido em Django.</p>
<p>Durante o curso, você aprenderá a criar e gerenciar dados, autenticação e relatórios.</p>
<a href="/" class="btn btn-secondary mt-3">Voltar</a>
{% endblock %}
```

## Agora temos o esqueleto da nossa aplicação!
