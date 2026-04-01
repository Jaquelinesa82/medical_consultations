# Medical Consultations API

## 🚀 Setup

### Com Docker
```bash
docker-compose up --build
```

## Rodar migrations
```bash
docker-compose exec web python manage.py migrate
```

## Rodar testes
```bash
docker-compose exec web python manage.py test
```