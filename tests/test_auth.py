import pytest
from fastapi.testclient import TestClient


def test_register_user(client: TestClient):
    """Тест регистрации пользователя"""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "newuser@example.com",
            "username": "newuser",
            "password": "newpassword123"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "newuser@example.com"
    assert data["username"] == "newuser"
    assert "password" not in data


def test_register_user_duplicate_email(client: TestClient, test_user):
    """Тест регистрации с существующим email"""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "anotheruser",
            "password": "password123"
        }
    )
    assert response.status_code == 400
    assert "Email already registered" in response.json()["detail"]


def test_register_user_duplicate_username(client: TestClient, test_user):
    """Тест регистрации с существующим username"""
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "another@example.com",
            "username": "testuser",
            "password": "password123"
        }
    )
    assert response.status_code == 400
    assert "Username already taken" in response.json()["detail"]


def test_login_success(client: TestClient, test_user):
    """Тест успешного входа"""
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials(client: TestClient):
    """Тест входа с неверными данными"""
    response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "nonexistent",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 401


def test_refresh_token(client: TestClient, test_user):
    """Тест обновления токена"""
    # Сначала получаем токены
    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    refresh_token = login_response.json()["refresh_token"]
    
    # Обновляем access токен
    response = client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": refresh_token}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_refresh_token_invalid(client: TestClient):
    """Тест обновления с неверным refresh токеном"""
    response = client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": "invalid_token"}
    )
    assert response.status_code == 401


def test_logout(client: TestClient, test_user):
    """Тест выхода из системы"""
    # Сначала получаем токены
    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    refresh_token = login_response.json()["refresh_token"]
    
    # Выходим из системы
    response = client.post(
        "/api/v1/auth/logout",
        json={"refresh_token": refresh_token}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Successfully logged out"


def test_me_endpoint(client: TestClient, test_user):
    """Тест получения информации о текущем пользователе"""
    # Сначала получаем токен
    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "username": "testuser",
            "password": "testpassword"
        }
    )
    access_token = login_response.json()["access_token"]
    
    # Получаем информацию о пользователе
    response = client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"


def test_me_endpoint_no_token(client: TestClient):
    """Тест получения информации без токена"""
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 403
