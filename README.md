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
$ pip install -r requirements.txt
```

### Configurando banco de dados e criando super usuário

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```

### Executando a aplicação

```bash
$ python manage.py runserver
```

Para testar a API, envie uma requisição POST para `http://localhost:8000/api/token/login/` com o seguinte JSON na body:

```
{
	"username": "nome_super_usuario",
	"password": "senha_super_usuario"
}
```

O resultado será algo como:

```
{
    "auth_token": "671cded32a1706fc52577c6fc33ad4353042f6e4"
}
```

Faça uma requisição POST para `http://localhost:8000/api/logs/` e passe o token para autorizar o acesso.
> Se estiver utilizando o Postman, por exemplo, na seção `Headers`, insira a key `Authorization` com value `Token token_gerado`. O resultado será uma lista vazia.

Acesse a documentação para saber como realizar o CRUD de Logs e como registrar novos usuários: `http://localhost:8000/api/documentation/`.

## Endpoints

Após executar a aplicação, você pode acessar a documentação da API, contendo os endpoints implementados, no endereço `http://localhost:8080/documentation/`.