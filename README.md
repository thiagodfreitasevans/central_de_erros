> Desafio final do Python AceleraDev - Codenation, com apoio da Stone.

# Central de Erros - Back-end (API)

Desenvolvimento de uma aplicação restful para registro e acesso a logs de erros registrados para possibilitar o monitoramento e auxiliar na tomada de decisão.

*A aplicação foi desenvolvida em conformidade com as instruções para o projeto final.* 

## Tecnologia

- [Python](https://www.python.org/) ```3.6```
- [Django](https://www.djangoproject.com/) ```3.0.8```
- [Django REST Framework](https://www.django-rest-framework.org/) ```3.11.0```
- [Swagger](https://swagger.io/) ```2.9.2```

## Instalação

Certifique-se de possuir o Python devidamente instalado em sua máquina.
> Instalando o Python: [https://www.python.org/](https://www.python.org/).

### Clonando o repositório:

```bash
$ git clone https://github.com/thiagodfreitasevans/central_de_erros.git
```

### Cronfigurando o ambiente virtual

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ cd central
$ pip install -r requirements.txt
```

### Configurando banco de dados e criando super usuário

```bash
$ python manage.py makemigrations
$ python migrate
$ python manage.py createsuperuser
```

### Executando a aplicação

```bash
$ python manage.py runserver
```

> Para testar a API, envie uma requisição POST para ```http://localhost:8000/api/token/login/´´´ com o seguinte JSON na body:

```
{
	"username": "nome_super_usuario",
	"password": "senha_super_usuario"
}
```

> O resultado será algo como:

```
{
    "auth_token": "671cded32a1706fc52577c6fc33ad4353042f6e4"
}
```

Utilize o token para acessar as sessão de Logs: ```http://localhost:8000/api/logs/´´´.

Você pode também pode criar usuários, para isso, acesse a documentação em ```http://localhost:8000/api/documentation/´´´.

## Endpoints

Após executar a aplicação, você pode acessar a documentação da API, contendo os endpoints implementados, no endereço ```http://localhost:8080/documentation/```.

## Deploy

Para fins de demonstração de funcionamento, foi feito o deploy da aplicação nas plataformas [Heroku](https://www.heroku.com/) e [Netlify](https://www.netlify.com/).

| Plataforma | Serviço | Link |
| :--- | :--- | :--- |
| Netlify | Front-end | [https://squad-1-front.netlify.com](https://squad-1-front.netlify.com)|
| Heroku | Back-end | *Sem acesso externo* |
| Heroku | Banco de Dados | *Sem acesso externo* |