# Deploy

Aqui estão os dados de referência para deploy de uma aplicação Django, de acordo
com as aulas do meu curso de Django na Udemy.

## Criando um servidor

Como vamos usar um servidor na nuvem (cloud server), é interessante que você
utilize algum serviço gratuito para isso. Recomendo a Google Cloud Platform.

Caso não tenha como usar a Google Cloud Platform, um servidor em máquina virtual
também funciona perfeitamente. Porém, não será possível disponibilizar a
aplicação online na Internet. VirtualBox (Windows, Linux e macOS intel),
Parallels (macOS M1), UTM (macOS M1), são alguns dos softwares mencionados
indicados para isso.

Siga as instruções da aula para criar um servidor na Google Cloud Platform.

### Chaves SSH

Para criar chaves ssh no seu computador, utilize o comando ssh-keygen. Se você
já tem chaves SSH no computador e por algum motivo queira usar outra, use o
comando:

```
ssh-keygen -t rsa -b 4096 -f CAMINHO+NOME_DA_CHAVE
```

Lembre-se que a pasta .ssh deve existir dentro da pasta do seu usuário para que
seja possível criar a chave SSH. Muito comum ocorrer erros no Windows por falta
dessa pasta.

Para conectar-se ao servidor usando uma chave SSH com caminho personalizado,
utilize:

```
ssh IP_OU_HOST -i CAMINHO+NOME_DA_CHAVE
```

### Ao entrar no servidor

A primeira coisa será atualizar tudo:

```
sudo apt update -y
```
```
sudo apt upgrade -y
```
```
sudo apt autoremove -y
```
```
sudo apt install build-essential -y
```
```
sudo apt install python3.9 python3.9-venv python3.9-dev -y
```
```
sudo apt install nginx -y
```
```
sudo apt install certbot python3-certbot-nginx -y
```
```
sudo apt install libpq-dev -y
```
```
sudo apt install curl -y
```
```
sudo timedatectl set-timezone America/Sao_Paulo
```

## Instalando o PostgreSQL

```
sudo apt install postgresql postgresql-contrib -y
```

Caso queira mais detalhes: https://youtu.be/VLpPLaGVJhI  
Mais avançado: https://youtu.be/FZaEukN_raA

### Configurações

```
sudo -u postgres psql
```
- Criando um super usuário
```sql
CREATE ROLE usuario WITH LOGIN SUPERUSER CREATEDB CREATEROLE PASSWORD 'senha';
```
- Criando a base de dados
```sql
CREATE DATABASE basededados WITH OWNER usuario;
```
- Dando permissões
```sql
GRANT ALL PRIVILEGES ON DATABASE basededados TO usuario;
```
## Saindo
```
\q
```
```
sudo systemctl restart postgresql
```

Caso queira mais detalhes: https://youtu.be/VLpPLaGVJhI  
Mais avançado: https://youtu.be/FZaEukN_raA

# Instalando e Configurando o git
```
sudo apt install git
```
- Altere o *Seu Nome* e o *seu_email@dominio.com* conforme seus dados
```
git config --global user.name 'Seu nome'
```
```
git config --global user.email 'seu_email@dominio.com'
```
```
git config --global init.defaultBranch main
```

# Criando um repositório no servidor

Um repositório bare é um repositório transitório (como se fosse um github).
Na raiz do projeto deve ser criada uma pasta, e dentro dela, iniciar um repositório bare.

```
mkdir -p ~/app_bare
```
```
cd ~/app_bare
```
```
git init --bare
```
```
cd ~
```

# Criando o repositório da aplicação

Criação do repositório original do git

```
mkdir -p ~/app_repo
```
```
cd ~/app_repo
```
```
git init
```
```
git remote add origin ~/app_bare
```
```
git add . && git commit -m 'Initial'
```
```
cd ~
```

- No seu computador local, adicione o bare como remoto:

Altere o trecho `username@ip_servidor` para o endereço do servidor
```
git remote add app_bare username@ip_servidor:~/app_bare
```
```
git push app_bare main
```

- No servidor, em app_repo, faça pull:

```
cd ~/app_repo
```
```
git pull origin main
```

# Criando o ambiente virtual

- Ainda no servidor, dentro da pasta app_repo:
```
python3.9 -m venv venv
```
```
. venv/bin/activate
```
```
pip install -r requirements.txt
```
```
pip install psycopg2
```

## Cria e configura o arquivo `.env`
```
cp .env-exemple .env
```
```
nano .env
```
- Faça as alterações pertinentes e depois salve o arquivo (CONTROL-O) e depois fecha (CONTROL-X)

## Valida se o Djando está funcionando:
```
python manage.py runserver
```
- Se confirmado, saia do servidor com `CONTROL-C`
```
python manage.py migrate
```
- Se for o caso, exclua o arquivo db.sqlite3(`rm db.sqlite3`), pois o postgresql será utilizado.

# Instalando e configurando o [Gunicorn](https://docs.gunicorn.org/en/stable/install.html)
O Gunicorn faz a comunicação entre o `nginx` e a nossa aplicação Django.

```
pip install gunicorn
```
- Seguir o passo a passo do Gist [gunicorn.md](https://gist.github.com/RenanMatias/6e1de435b53bed4df969c14007a7fc49)

# Configurando o [NGINX](https://www.nginx.com/)
O NGINX é um servidor web que substituará o `runserver` do Django.

## HTTP
- Fazer as alterações de acordo com o Gists [Configuração do NGINX HTTP](https://gist.github.com/RenanMatias/d5d24e11e008dba99b3e3f56f92add14)
- Copiar todo o arquivo alterado;
```
sudo nano /etc/nginx/sites-available/<nome_do_projeto>
```
- Colar
- Salve o arquivo (CONTROL-O) e depois fecha (CONTROL-X)
```
sudo rm /etc/nginx/sites-enabled/default
```
```
sudo ln -s /etc/nginx/sites-available/<nome_do_projeto> /etc/nginx/sites-enabled/<nome_do_projeto>
```
- Tetar se a configuração está certa
```
sudo nginx -t
```
- O retorno deve ser:
  - `nginx: the configuration file /etc/nginx/nginx.conf syntax is ok`
  - `nginx: configuration file /etc/nginx/nginx.conf test is successful`
```
sudo systemctl restart nginx
```
