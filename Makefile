.PHONY: help install test run docker-build docker-run docker-stop clean migrate superuser

help: ## Показать справку
	@echo "Доступные команды:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## Установить зависимости
	pip install -r requirements.txt

test: ## Запустить тесты
	pytest -v

test-cov: ## Запустить тесты с покрытием
	pytest --cov=app --cov-report=html

run: ## Запустить приложение локально
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

docker-build: ## Собрать Docker образ
	docker-compose build

docker-run: ## Запустить с Docker Compose
	docker-compose up -d

docker-stop: ## Остановить Docker Compose
	docker-compose down

docker-logs: ## Показать логи Docker
	docker-compose logs -f app

clean: ## Очистить временные файлы
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

migrate: ## Применить миграции
	alembic upgrade head

migrate-create: ## Создать новую миграцию
	@read -p "Введите описание миграции: " description; \
	alembic revision --autogenerate -m "$$description"

superuser: ## Создать суперпользователя
	python scripts/create_superuser.py

init: ## Инициализация проекта (установка + миграции + суперпользователь)
	make install
	make migrate
	make superuser

dev: ## Запуск в режиме разработки
	make install
	make migrate
	make run
