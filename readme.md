## Dashboard do Dataset Titanic com Django

Se você não fez o tutorial flashcards fazer antes: https://github.com/leandrocl2005/flashcards

## Repositório do projeto

- https://github.com/leandrocl2005/titanic-dashboard-django

### Commit f638233

## Setup inicial

- Crie uma pasta chamada *titanic* (será a pasta raiz do projeto)
- Abra esta pasta com o Vs Code
- Crie um ambiente virtual: `python -m venv env`
- Ative o ambiente virtual: `. env/Scripts/activate`
- Conecte seu VS code ao seu ambiente virtual
- Adicione a raíz do projeto as configurações .vscode (ver repositório flashcards)
- Adicione a raíz do projeto o arquivo .gitignore (ver repositório flashcards)
- Instale o django: `pip install django`
- Crie o projeto Django: `django-admin startproject config .`
- Crie o app flash cards: `python manage.py startapp dashboard`
- Adicione 'dashboard' em *config/settings.py* em `INSTALLED_APPS`
- Teste se a página do Django está sendo renderizada: `python manage.py runserver`
- Crie uma pasta *templates* na raiz do projeto
- No settings troque `"DIRS": [],` por `"DIRS": [BASE_DIR / "templates"],`
- Em *config/urls* adicionar `path("", include("dashboard.urls")),`
- Criar um arquivo *dashboard/urls.py* com o código:
```python
from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
]
```
- Em *dashboard/views.py* colocar o código
```python
from django.shortcuts import render

def index(request):
    return render(request, "dashboard/index.html")
```
- Em *templates* adicionar a pasta *dashboard*
- Em *templates/dashboard* mover o arquivo *index.html* para dentro
- Teste se o index.html está sendo renderizado: `python manage.py runserver`
- Em *config/urls* adicionar `urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)`
- Em *config/settings.py* adicionar `STATICFILES_DIRS = [BASE_DIR / "static"]`
- Colocar a tag jinja `{% load static %}` no começo de *index.html*
- Alterar `href="static/css/styles.css"` para `href="{% static 'css/styles.css' %}"`
- Alterar `src="./static/js/scripts.js"` para `src="{% static 'js/scripts.js' %}"`
- Alterar `src="/static/assets/titanic.png"` para `src="{% static 'assets/titanic.png' %}"`
- Instale pandas: `pip install pandas`
- Veja a lista de bibliotecas instaladas: `pip freeze`
- Crie o arquivo *requiments.txt* com as dependências do projeto

## Commit 47ddad9

- Enviar dados do CSV para o contexto da view e, então, para o template! (ver vídeo)

## Commit 7b624fd

- Enviar dados do DB para o contexto da view e, então, para o template! (ver vídeo)

## Commit 86448e0

- Completar o código em dashboard/views.py para enviar todo o contexto com dados extraídos do bando de dados.

- para rodar o projeto:
- Set-ExecutionPolicy RemoteSigned -Scope Process (dá permissão)
- . env/Scripts/activate   (ativa o ambiente virtual)
- python manage.py runserver   (ativa o servidor)
- "C:\Users\jamil\projeto titanic\titanic-dashboard-django" (caminho para o projeto)