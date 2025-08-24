#!/usr/bin/env python3
"""
Скрипт для создания суперпользователя
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_user, get_user_by_email, get_user_by_username
from app.schemas import UserCreate


def create_superuser():
    """Создание суперпользователя"""
    db = SessionLocal()
    try:
        # Проверяем, существует ли уже суперпользователь
        existing_user = get_user_by_email(db, "admin@example.com")
        if existing_user:
            print("Суперпользователь уже существует!")
            return
        
        # Создаем суперпользователя
        superuser_data = UserCreate(
            email="admin@example.com",
            username="admin",
            password="admin123"
        )
        
        user = create_user(db=db, user=superuser_data)
        
        # Делаем пользователя суперпользователем
        user.is_superuser = True
        db.commit()
        
        print("✅ Суперпользователь успешно создан!")
        print(f"Email: {user.email}")
        print(f"Username: {user.username}")
        print("Password: admin123")
        print("\n⚠️  Не забудьте изменить пароль в продакшене!")
        
    except Exception as e:
        print(f"❌ Ошибка при создании суперпользователя: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    create_superuser()
