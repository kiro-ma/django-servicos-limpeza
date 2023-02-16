# django-servicos-limpeza
Sistema para gerenciamento de uma loja de serviços de limpeza.

# Guia de instalação
1 - Após clonar o repositório, execute o arquivo "run_server.bat", ele irá iniciar o ambiente virtual Python e o servidor Django no localhost (será especificada a porta no cmd).  
2 - Crie um arquivo .env dentro da aplicação "mysite" com os seguintes campos:  

    SECRET_KEY=*sua chave secreta django, caso não tenha, entrar em contato comigo (Kiro)*
    DB_NAME=limpeza_db
    DB_USER=*usuario pgadmin*
    DB_PASSWORD="senha pgadmin"
    DB_HOST=localhost
    DB_PORT=5432

3 - Vá no PgAdmin e crie uma database chamada "limpeza_db".  
4 - Pare o servidor Djando e rode os comandos "python manage.py makemigrations" e "python manage.py migrate"  
5 - Inicie novamente o servidor Django com o comando "python manage.py runserver". Acesse 127.0.0.1:*PORTA*  

# Começando a usar o sistema

## Criar um SuperUser
Rode o comando "python manage.py createsuperuser" e crie um usuário administrador para começar a utilizar a aplicação.

## Criar um Atendente
Como superuser, haverá a opção de criar um usuário, crie um usuário do tipo "Atendente" e um do tipo "Helper"

## Criado por Kiro Marcell, disponível no [GitHub](https://github.com/kiro-ma).
