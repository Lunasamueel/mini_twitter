# 📘 Projeto Django REST API - Backend

## Este projeto é uma API REST construída com Django e Django REST Framework, com autenticação JWT e documentação integrada via Swagger.

#🚀 Como rodar o projeto

### Clone o repositório

### Crie um ambiente virtual

### python -m venv venv

### Ative o ambiente virtualNo Windows:

### venv\Scripts\activate

# crie o arquivo .env:
  ## .env
    DATABASE_URL=postgres://postgres:postgres@db:5432/postgres
    DEBUG=True
    SECRET_KEY=django-insecure-h^gqby#ugeu7tgt!^z#$1z3(x02p3a05$nitpfghl&$4bx!o0j
    DB_NAME=mini_twitter_db
    DB_USER=twitter_user
    DB_PASS=123456
    DB_HOST=localhost
    DB_PORT=5432


# Instale as dependências

## pip install -r requirements.txt

### (Opcional) Instale o drf-yasg, caso não esteja incluso no requirements.txt

### pip install drf-yasg

# 📚 Documentação da API

## Todos os endpoints estão documentados e disponíveis via Swagger:

## 🔗 http://localhost:8000/swagger/

# 🔐 Autenticação JWT

## Para testar os endpoints autenticados, você precisa obter um token JWT.

# ★ Exemplo de usuário para autenticação

## Usuário: samuel Senha: 123456

## Como autenticar no Swagger

## Clique em "Authorize" no topo direito.

## Insira o token JWT assim:

## Bearer SEU_TOKEN_AQUI

## Lembre-se de incluir a palavra Bearer antes do token.

# 📂 Funcionalidades

## Registro e login de usuários

### Autenticação com JWT

### Sistema de seguir e deixar de seguir usuários

### Publicações com conteúdo e imagem

### Curtidas em posts com atualização em tempo real (like/unlike)

### Feed com paginação dos posts de usuários seguidos

# 🛠 Requisitos

## Python 3.9+

## Django 4+

## Django REST Framework

## Simple JWT

## drf-yasg (Swagger)

# Reactjs - Frontend

## baixe o projeto

## execute npm install

## execute npm run dev

## o projeto deve rodar na porta http://localhost:5173/



