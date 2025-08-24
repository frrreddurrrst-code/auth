from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # База данных - используем SQLite для локальной разработки
    database_url: str = "sqlite:///./auth_service.db"
    
    # JWT настройки
    secret_key: str = "your-super-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Настройки приложения
    app_name: str = "Auth Service"
    app_version: str = "1.0.0"
    debug: bool = False
    
    class Config:
        env_file = ".env"


settings = Settings()
