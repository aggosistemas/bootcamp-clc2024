# Use uma Imagem Official do Python
FROM python:3

# Declarando a váriavel do nome do arquivo de configuração do NewRelic
ENV NEW_RELIC_CONFIG_FILE=/home/myapp/newrelic.ini  NEW_RELIC_LICENSE_KEY=licensekey

# Adicionando um usuário de sistema
RUN adduser --system --home /home/myapp  myapp
USER myapp

# Definindo o diretório onde a aplicação será armazenada
WORKDIR /home/myapp

# Definindo o local onde o binário do gunicorn é instalado
ENV PATH="/home/myapp/.local/bin:${PATH}"

# Copiar os arquivos da pasta local para dentro do container
COPY --chown=root:root --chmod=644 newrelic.ini app.py requirements.txt /home/myapp/

# Instalar as dependências de Python de acordo com o que foi desenvolvido na aplicação e que está declarado no arquivo requirements.txt.
RUN pip install --user --trusted-host pypi.python.org -r requirements.txt

# Garante que será iniciado a aplicação.
CMD ["newrelic-admin", "run-program", "gunicorn", "app:app"]