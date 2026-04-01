# Imagem base Python 3.12
FROM python:3.12-slim

# Diretório de trabalho no container
WORKDIR /app

# Copia arquivos necessários para instalar dependências
COPY pyproject.toml poetry.lock* README.md /app/

# Instala o Poetry
RUN pip install --no-cache-dir poetry

# Instala dependências sem criar virtualenv e sem instalar o próprio projeto
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copia o código fonte
COPY . /app/

# Comando para rodar a aplicação
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]