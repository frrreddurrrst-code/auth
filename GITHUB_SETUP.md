# 📝 Пошаговая инструкция по загрузке на GitHub

## 1. Установка Git

### Windows:
1. Скачай Git с официального сайта: https://git-scm.com/download/win
2. Установи с настройками по умолчанию
3. Перезапусти PowerShell/командную строку

### Проверка установки:
```bash
git --version
```

## 2. Настройка Git (первый раз)

```bash
git config --global user.name "Твое Имя"
git config --global user.email "твой.email@example.com"
```

## 3. Инициализация репозитория

```bash
# В папке проекта
git init
git add .
git commit -m "Initial commit: Auth Service with FastAPI"
```

## 4. Создание репозитория на GitHub

1. Перейди на https://github.com
2. Войди в свой аккаунт
3. Нажми зеленую кнопку "New" или "+" → "New repository"
4. Заполни поля:
   - **Repository name**: `auth-service-fastapi` (или любое другое название)
   - **Description**: `Modern authentication service built with FastAPI, PostgreSQL, and JWT tokens`
   - **Visibility**: Public (или Private, если хочешь)
   - **НЕ ставь галочки** на "Add a README file", "Add .gitignore", "Choose a license"
5. Нажми "Create repository"

## 5. Подключение к GitHub

GitHub покажет команды. Выполни их:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

**Замени:**
- `YOUR_USERNAME` - твое имя пользователя на GitHub
- `YOUR_REPO_NAME` - название репозитория, которое ты создал

## 6. Проверка

Перейди на страницу твоего репозитория на GitHub - там должны появиться все файлы проекта.

## 7. Дополнительные файлы для продакшена

### Создание Procfile для Heroku:
```bash
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" > Procfile
```

### Создание runtime.txt:
```bash
echo "python-3.12.0" > runtime.txt
```

### Обновление requirements.txt для продакшена:
Добавь в `requirements.txt`:
```
psycopg2-binary==2.9.9
```

### Закоммить изменения:
```bash
git add .
git commit -m "Add deployment files"
git push
```

## 8. Что получится

После загрузки у тебя будет:
- ✅ Полноценный репозиторий на GitHub
- ✅ Готовая к развертыванию кодовая база
- ✅ Документация для рекрутера
- ✅ Возможность деплоя на Heroku/Docker

## 9. Ссылки для рекрутера

После загрузки можешь отправить рекрутеру:
- **GitHub репозиторий**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`
- **Документация**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/README.md`
- **Быстрый старт**: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/blob/main/QUICK_START.md`

## 10. Демонстрация

Рекрутер сможет:
1. Посмотреть код в репозитории
2. Клонировать проект: `git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git`
3. Запустить локально по инструкции в README
4. Увидеть API документацию по адресу http://localhost:8000/docs

## Полезные команды Git

```bash
# Проверить статус
git status

# Посмотреть историю коммитов
git log --oneline

# Добавить изменения
git add .

# Создать коммит
git commit -m "Описание изменений"

# Отправить на GitHub
git push

# Получить изменения с GitHub
git pull
```
