# Aula 3 - Modelagem inicial do banco de dados com SQLite

- Hoje vamos criar a nossa primeira tabela do banco de dados! Ela irá armazenar as informações sobre nossas transações financeiras, divididas entre receitas (R) e despesas (D)

<br>

# Criando nosso app de finanças

- Começamos com o mesmo comando que usamos para criar os outros apps:

```python
python manage.py startapp financas
```

<br>

- Registramos nosso novo aplicativo no `settings.py`, assim como fizemos com o aplicativo `base` na aula passada.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base',
    'financas',
]
```

<br>

# Modelagem e criação da nossa primeira tabela (Transação)

- No arquivo `models.py` da pasta `financas` escreva:

```python
from django.db import models
from django.contrib.auth.models import User

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('R', 'Receita'),
        ('D', 'Despesa'),
    ]

    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    valor = models.FloatField()
    data = models.DateField()
    categoria = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao} - {self.get_tipo_display()} ({self.valor})"
```

<br>

# Criação e aplicação das migrações/migrations

- De volta a pasta onde está o seu arquivo `manage.py` execute:

```python
python manage.py makemigrations financas
```

- E em seguida:

```python
python manage.py migrate
```

<br>

# Registro do nosso modelo no painel de administrador (Django Admin)

- Na pasta `financas`, no arquivo `admin.py` escreva:

```python
from django.contrib import admin
from .models import Transacao

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'tipo', 'valor', 'data', 'categoria', 'usuario')
    list_filter = ('tipo', 'categoria')
    search_fields = ('descricao',)
```

<br>

# Criação do superusuário/usuário administrador

- Na pasta onde está seu arquivo `manage.py` execute o seguinte comando:

```python
python manage.py createsuperuser
```

- Nas informações, coloque:

```
Usuário: admin
Email: Deixe em branco
Senha: 123456
```

- Iniciamos mais uma vez o servidor:

```python
python manage.py runserver
```

- Vamos acessar o painel de administração do Django adicionando `admin` ao endereço do nosso servidor local.

- Faça login com o superusuário que você acabou de criar.

- Crie uma nova transação na tabela de transações.

- Se tudo der certo, parabéns, agora você tem um banco de dados configurado corretamente!

# Referências

- [O que é BANCO DE DADOS e porque INTERESSA APRENDER isso?](https://www.youtube.com/watch?v=XfO3TRvESBo)

- [Campos de modelo Django - Casos de uso comuns e como eles funcionam](https://prt.python-3.com/?p=4210)