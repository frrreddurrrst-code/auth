# 🚀 Развертывание проекта

## GitHub

### 1. Инициализация Git репозитория
```bash
git init
git add .
git commit -m "Initial commit: Auth Service with FastAPI"
```

### 2. Создание репозитория на GitHub
1. Перейди на https://github.com
2. Нажми "New repository"
3. Назови репозиторий (например: `auth-service-fastapi`)
4. НЕ ставь галочки (README, .gitignore, license)
5. Нажми "Create repository"

### 3. Подключение к GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## Heroku (бесплатный хостинг)

### 1. Создание Procfile
```bash
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile
```

### 2. Создание runtime.txt
```bash
echo "python-3.12.0" > runtime.txt
```

### 3. Обновление requirements.txt для продакшена
```bash
# Добавь в requirements.txt:
psycopg2-binary==2.9.9
```

### 4. Настройка переменных окружения в Heroku
```bash
heroku config:set SECRET_KEY="your-super-secret-key-change-in-production"
heroku config:set DATABASE_URL="postgresql://..."
```

### 5. Деплой
```bash
heroku create your-app-name
git add .
git commit -m "Add Heroku deployment files"
git push heroku main
```

## Docker Hub

### 1. Сборка образа
```bash
docker build -t your-username/auth-service .
```

### 2. Загрузка на Docker Hub
```bash
docker push your-username/auth-service
```

### 3. Запуск из Docker Hub
```bash
docker run -p 8000:8000 your-username/auth-service
```

## Локальное развертывание

### 1. Клонирование
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Установка зависимостей
```bash
python -m pip install -r requirements.txt
```

### 3. Запуск
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Переменные окружения

Создай файл `.env` в корне проекта:

```env
# База данных
DATABASE_URL=sqlite:///./auth_service.db

# JWT настройки
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Настройки приложения
APP_NAME=Auth Service
APP_VERSION=1.0.0
DEBUG=false
```

## Проверка работоспособности

### 1. Health check
```bash
curl http://localhost:8000/health
```

### 2. API документация
Открой в браузере: http://localhost:8000/docs

### 3. Тесты
```bash
python -m pytest tests/ -v
```

## Структура для GitHub

```
auth-service/
├── app/                    # Основной код
├── tests/                  # Тесты
├── alembic/               # Миграции БД
├── scripts/               # Скрипты
├── requirements.txt       # Зависимости
├── Dockerfile            # Docker образ
├── docker-compose.yml    # Docker Compose
├── README.md             # Основная документация
├── QUICK_START.md        # Быстрый старт
├── DEPLOYMENT.md         # Инструкции по развертыванию
├── .gitignore           # Исключения Git
├── env.example          # Пример переменных окружения
└── Makefile             # Команды для разработки
```
