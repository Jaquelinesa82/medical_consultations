# Medical Consultations API

API para gerenciamento de consultas médicas construída com Django e Django REST Framework.

---

## 🚀 Setup

### 🔹 Com Docker

```bash
docker-compose up --build
```

A aplicação estará disponível em:
👉 http://localhost:8000

---

### 🔹 Com Poetry (sem Docker)

```bash
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver
```

---

## 🧪 Testes

### Com Docker

```bash
docker-compose exec web python manage.py test
```

### Com Poetry

```bash
poetry run python manage.py test
```

---

## 🧹 Qualidade de código

Este projeto utiliza:

* Ruff (lint + formatter)
* pre-commit

Rodar manualmente:

```bash
poetry run ruff check .
poetry run ruff format .
poetry run pre-commit run --all-files
```

---

## ⚙️ CI

O projeto utiliza GitHub Actions para:

* Executar migrations
* Rodar testes automaticamente
* Validar lint com Ruff
* Garantir padrão de código com pre-commit

---

## 🗄️ Banco de dados

Por padrão utiliza PostgreSQL.

Configuração via variável de ambiente:

```
DATABASE_URL=postgres://postgres:postgres@localhost:5432/medical_db
```

---

## 🔍 Health Check

Endpoint para verificação da API:

```
GET /health/
```

Resposta esperada:

```json
{
  "status": "ok"
}
```

---

## 📁 Estrutura do projeto

```
core/               # Configuração do projeto
professionals/      # App principal
tests/              # Testes automatizados
```
