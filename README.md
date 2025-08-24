# Сервис Авторизации

Современный сервис авторизации, построенный на FastAPI с использованием PostgreSQL и JWT токенов.

## 🚀 Технологии

- **Python 3.12** - основной язык программирования
- **FastAPI** - современный веб-фреймворк для создания API
- **PostgreSQL** - реляционная база данных
- **SQLAlchemy** - ORM для работы с базой данных
- **Alembic** - система миграций базы данных
- **JWT** - JSON Web Tokens для аутентификации
- **bcrypt** - хеширование паролей
- **Docker** - контейнеризация приложения
- **Pytest** - тестирование

## 📋 Функциональность

### Аутентификация
- ✅ Регистрация пользователей
- ✅ Вход в систему (логин)
- ✅ JWT токены (access + refresh)
- ✅ Обновление токенов
- ✅ Выход из системы
- ✅ Получение информации о текущем пользователе

### Управление пользователями
- ✅ CRUD операции для пользователей
- ✅ Активация/деактивация пользователей
- ✅ Роли пользователей (обычный пользователь/суперпользователь)
- ✅ Валидация данных с Pydantic

### Безопасность
- ✅ Хеширование паролей с bcrypt
- ✅ JWT токены с настраиваемым временем жизни
- ✅ Refresh токены с возможностью отзыва
- ✅ CORS настройки
- ✅ Валидация входных данных

## 🏗️ Архитектура

```
app/
├── __init__.py
├── main.py              # Основное приложение FastAPI
├── config.py            # Конфигурация приложения
├── database.py          # Настройка базы данных
├── models.py            # SQLAlchemy модели
├── schemas.py           # Pydantic схемы
├── auth.py              # Аутентификация и авторизация
├── crud.py              # CRUD операции
└── api/
    ├── __init__.py
    ├── api.py           # Основной API роутер
    └── endpoints/
        ├── __init__.py
        ├── auth.py      # Endpoints аутентификации
        └── users.py     # Endpoints управления пользователями
```

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone <repository-url>
cd auth-service
```

### 2. Запуск с Docker Compose (рекомендуется)
```bash
# Запуск всех сервисов
docker-compose up -d

# Просмотр логов
docker-compose logs -f app
```

### 3. Ручная установка

#### Установка зависимостей
```bash
pip install -r requirements.txt
```

#### Настройка базы данных
```bash
# Создание миграций
alembic revision --autogenerate -m "Initial migration"

# Применение миграций
alembic upgrade head
```

#### Запуск приложения
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 📚 API Документация

После запуска приложения документация доступна по адресам:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Основные endpoints

#### Аутентификация
- `POST /api/v1/auth/register` - Регистрация пользователя
- `POST /api/v1/auth/login` - Вход в систему
- `POST /api/v1/auth/refresh` - Обновление токена
- `POST /api/v1/auth/logout` - Выход из системы
- `GET /api/v1/auth/me` - Информация о текущем пользователе

#### Управление пользователями
- `GET /api/v1/users/` - Список пользователей (только для суперпользователей)
- `POST /api/v1/users/` - Создание пользователя (только для суперпользователей)
- `GET /api/v1/users/{user_id}` - Получение пользователя по ID
- `PUT /api/v1/users/{user_id}` - Обновление пользователя
- `DELETE /api/v1/users/{user_id}` - Удаление пользователя (только для суперпользователей)
- `POST /api/v1/users/{user_id}/activate` - Активация пользователя
- `POST /api/v1/users/{user_id}/deactivate` - Деактивация пользователя

## 🔧 Конфигурация

### Переменные окружения

Создайте файл `.env` в корне проекта:

```env
# База данных
DATABASE_URL=postgresql://auth_user:auth_password@localhost:5432/auth_db

# JWT настройки
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Настройки приложения
APP_NAME=Auth Service
APP_VERSION=1.0.0
DEBUG=false
```

### Docker Compose

Основные настройки в `docker-compose.yml`:
- **Порт приложения**: 8000
- **Порт PostgreSQL**: 5432
- **База данных**: auth_db
- **Пользователь БД**: auth_user
- **Пароль БД**: auth_password

## 🧪 Тестирование

### Запуск тестов
```bash
# Все тесты
pytest

# С подробным выводом
pytest -v

# С покрытием кода
pytest --cov=app

# Конкретный тест
pytest tests/test_auth.py::test_register_user
```

### Структура тестов
```
tests/
├── __init__.py
├── conftest.py          # Конфигурация и фикстуры
└── test_auth.py         # Тесты аутентификации
```

## 📦 Миграции базы данных

### Создание миграции
```bash
alembic revision --autogenerate -m "Описание изменений"
```

### Применение миграций
```bash
# Применить все миграции
alembic upgrade head

# Применить конкретную миграцию
alembic upgrade <revision>

# Откатить миграцию
alembic downgrade -1
```

### Просмотр истории миграций
```bash
alembic history
```

## 🔒 Безопасность

### Рекомендации для продакшена

1. **Измените SECRET_KEY** на уникальный и сложный ключ
2. **Настройте CORS** для конкретных доменов
3. **Используйте HTTPS** в продакшене
4. **Настройте rate limiting** для защиты от брутфорса
5. **Используйте переменные окружения** для конфиденциальных данных
6. **Настройте логирование** для мониторинга
7. **Регулярно обновляйте зависимости**

### Хеширование паролей

Пароли хешируются с использованием bcrypt с автоматической солью. Это обеспечивает:
- Защиту от rainbow table атак
- Медленное хеширование для защиты от брутфорса
- Автоматическую генерацию соли

### JWT токены

- **Access токены**: короткое время жизни (30 минут по умолчанию)
- **Refresh токены**: длительное время жизни (30 дней)
- **Отзыв токенов**: refresh токены можно отозвать при выходе

## 📊 Мониторинг

### Health check
```bash
curl http://localhost:8000/health
```

### Логи
```bash
# Docker Compose
docker-compose logs -f app

# Локальный запуск
uvicorn app.main:app --log-level debug
```

## 🤝 Разработка

### Структура проекта
```
.
├── app/                 # Основной код приложения
├── tests/              # Тесты
├── alembic/            # Миграции базы данных
├── requirements.txt    # Python зависимости
├── Dockerfile         # Docker образ
├── docker-compose.yml # Docker Compose конфигурация
├── alembic.ini        # Конфигурация Alembic
└── README.md          # Документация
```

### Стиль кода
- **Black** для форматирования
- **isort** для сортировки импортов
- **flake8** для линтинга
- **mypy** для проверки типов

### Git hooks
Рекомендуется настроить pre-commit hooks для автоматической проверки кода.

## 📝 Лицензия

MIT License

## 🤝 Вклад в проект

1. Fork репозитория
2. Создайте feature branch (`git checkout -b feature/amazing-feature`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в branch (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📞 Поддержка

Если у вас есть вопросы или проблемы, создайте issue в репозитории.
