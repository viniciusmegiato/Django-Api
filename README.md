# Microserviços, API Gateway e Autenticação JWT com Django

![image](https://github.com/viniciusmegiato/Django-Api/assets/82332528/56cbe1d9-8a90-44d9-a263-c9e06fce95eb)
* Conceitos de APi Rest, gateway e JWT foram implementados nesse projeto, que foi feito em python, utilizando django.
* Também introduzi testes para a API.

# Execução
* Clone o repositório e baixe as bibliotecas através do requirements.txt
* Criar uma venv seria interessante para não possuir possíves conflitos de versões
* Após a instalação, execute o projeto: ```py manage.py runserver```
* O projeto conta com um usuário cadastrado, então faça o login, se necessário, na rota  ```http://127.0.0.1:8000/admin```
* Dados de login -> Usuário: admin, Senha: admin
* Página inicial ```http://127.0.0.1:8000/``` já possui alguns links para as rotas na aplicação

# Autenticação JWT
* Definido no settings que o token possui validação de 30 minutos e o refresh de 1 hora.
* Para obter o token para testar api em algum programa (exemplo: insonmia)
  * Rota Token 
    * Definir o header como ```Content-Type``` e o value como ```application/json```
    * Definir em json o acesso do usuário e senha
    * Acessar a rota ```http://127.0.0.1:8000/token/```
    * Irá retornar um access e um refresh
  * Rota Refresh Token
    * Definir o header como ```Content-Type``` e o value como ```application/json```
    * Definir em json o acesso do token usando o retorno do refresh no passo Rota Token ```{"refresh": "valor_token_refresh"}```
    * Acessar a rota ```http://127.0.0.1:8000/token/refresh```
    * Irá retornar o access
  * Rota dos endpoints
    * Definir o header como ```Content-Type``` e o value como ```application/json```
    * Definir um segundo valor do header como ```Authorization``` e o value com o retorno do access no passo Rota Refresh Token
    * Irá retornar informações da api conforme o endpoint usado.

# Documentação
![image](https://github.com/viniciusmegiato/Django-Api/assets/82332528/de50117e-7305-4aba-a90f-a82ae3a82ca9)
Acesse: http://127.0.0.1:8000/swagger/

# Exemplos de Requisição
* GET Produtos <h4>
![image](https://github.com/viniciusmegiato/Django-Api/assets/82332528/644917c7-c781-4f24-a203-0038b1052ef8)

* Retorno <h4>
![image](https://github.com/viniciusmegiato/Django-Api/assets/82332528/3c2a2550-46c5-4ccd-bdb2-28df05f852c4)

* GET Produtos ID <h4>
![image](https://github.com/viniciusmegiato/Django-Api/assets/82332528/fee7a596-1ef8-468a-a18a-2162af701a80)

* Retorno <h4>
![image](https://github.com/viniciusmegiato/Django-Api/assets/82332528/4d1ddfcb-eb59-4230-aed8-2b04acd31852)

