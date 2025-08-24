import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_db, Base
from app.models import User
from app.auth import get_password_hash

# Создаем тестовую базу данных в памяти
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создаем таблицы для тестов
Base.metadata.create_all(bind=engine)


def override_get_db():
    """Переопределяем зависимость для получения тестовой сессии БД"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


# Подменяем зависимость
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    """Фикстура для тестового клиента"""
    with TestClient(app) as c:
        yield c


@pytest.fixture
def db_session():
    """Фикстура для тестовой сессии БД"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def test_user(db_session):
    """Фикстура для тестового пользователя"""
    user = User(
        email="test@example.com",
        username="testuser",
        hashed_password=get_password_hash("testpassword"),
        is_active=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


@pytest.fixture
def test_superuser(db_session):
    """Фикстура для тестового суперпользователя"""
    user = User(
        email="admin@example.com",
        username="admin",
        hashed_password=get_password_hash("adminpassword"),
        is_active=True,
        is_superuser=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user
