# 🚀 Быстрый старт

## Установка и запуск

### 1. Установка зависимостей
```bash
python -m pip install -r requirements.txt
```

### 2. Запуск сервера
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Открыть в браузере
- **API документация**: http://localhost:8000/docs
- **ReDoc документация**: http://localhost:8000/redoc
- **Health check**: http://localhost:8000/health

## Тестирование API

### Регистрация пользователя
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "password": "testpassword123"
  }'
```

### Вход в систему
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpassword123"
  }'
```

### Получение информации о пользователе (с токеном)
```bash
curl -X GET "http://localhost:8000/api/v1/auth/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Docker (альтернативный способ)

### Запуск с Docker Compose
```bash
docker-compose up -d
```

### Остановка
```bash
docker-compose down
```

## Структура проекта

```
собес/
├── app/                    # Основной код приложения
│   ├── main.py            # Точка входа FastAPI
│   ├── config.py          # Конфигурация
│   ├── database.py        # Настройка БД
│   ├── models.py          # SQLAlchemy модели
│   ├── schemas.py         # Pydantic схемы
│   ├── auth.py            # Аутентификация
│   ├── crud.py            # CRUD операции
│   └── api/               # API endpoints
├── tests/                 # Тесты
├── alembic/               # Миграции БД
├── requirements.txt       # Python зависимости
├── docker-compose.yml     # Docker конфигурация
├── Dockerfile            # Docker образ
└── README.md             # Полная документация
```

## База данных

- **Локальная разработка**: SQLite (`auth_service.db`)
- **Docker**: PostgreSQL
- **Тесты**: SQLite в памяти

## Основные endpoints

### Аутентификация
- `POST /api/v1/auth/register` - Регистрация
- `POST /api/v1/auth/login` - Вход
- `POST /api/v1/auth/refresh` - Обновление токена
- `POST /api/v1/auth/logout` - Выход
- `GET /api/v1/auth/me` - Информация о пользователе

### Управление пользователями
- `GET /api/v1/users/` - Список пользователей
- `GET /api/v1/users/{id}` - Получение пользователя
- `PUT /api/v1/users/{id}` - Обновление пользователя
- `DELETE /api/v1/users/{id}` - Удаление пользователя

## Безопасность

- ✅ JWT токены (access + refresh)
- ✅ Хеширование паролей (bcrypt)
- ✅ Валидация данных (Pydantic)
- ✅ CORS настройки
- ✅ Роли пользователей (обычный/суперпользователь)

## Технологии

- **Python 3.12+**
- **FastAPI** - веб-фреймворк
- **SQLAlchemy** - ORM
- **Alembic** - миграции
- **JWT** - аутентификация
- **bcrypt** - хеширование паролей
- **Docker** - контейнеризация
- **PostgreSQL/SQLite** - базы данных
