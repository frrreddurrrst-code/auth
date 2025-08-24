from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_active_user, get_current_superuser
from app.crud import (
    get_user, get_users, create_user, update_user, delete_user,
    deactivate_user, activate_user, get_user_by_email, get_user_by_username
)
from app.schemas import UserCreate, User, UserUpdate
from app.models import User as UserModel

router = APIRouter()


@router.get("/", response_model=List[User])
def read_users(
    skip: int = 0,
    limit: int = 100,
    current_user: UserModel = Depends(get_current_superuser),
    db: Session = Depends(get_db)
):
    """Получение списка пользователей (только для суперпользователей)"""
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_new_user(
    user: UserCreate,
    current_user: UserModel = Depends(get_current_superuser),
    db: Session = Depends(get_db)
):
    """Создание нового пользователя (только для суперпользователей)"""
    # Проверяем, что email не занят
    if get_user_by_email(db, email=user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Проверяем, что username не занят
    if get_user_by_username(db, username=user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    
    return create_user(db=db, user=user)


@router.get("/{user_id}", response_model=User)
def read_user(
    user_id: int,
    current_user: UserModel = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Получение пользователя по ID (пользователь может получить только свои данные, суперпользователь - любые)"""
    if current_user.id != user_id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    user = get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


@router.put("/{user_id}", response_model=User)
def update_user_data(
    user_id: int,
    user_update: UserUpdate,
    current_user: UserModel = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """Обновление пользователя (пользователь может обновить только свои данные, суперпользователь - любые)"""
    if current_user.id != user_id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    
    user = update_user(db, user_id=user_id, user_update=user_update)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


@router.delete("/{user_id}")
def delete_user_data(
    user_id: int,
    current_user: UserModel = Depends(get_current_superuser),
    db: Session = Depends(get_db)
):
    """Удаление пользователя (только для суперпользователей)"""
    success = delete_user(db, user_id=user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {"message": "User deleted successfully"}


@router.post("/{user_id}/deactivate", response_model=User)
def deactivate_user_data(
    user_id: int,
    current_user: UserModel = Depends(get_current_superuser),
    db: Session = Depends(get_db)
):
    """Деактивация пользователя (только для суперпользователей)"""
    user = deactivate_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


@router.post("/{user_id}/activate", response_model=User)
def activate_user_data(
    user_id: int,
    current_user: UserModel = Depends(get_current_superuser),
    db: Session = Depends(get_db)
):
    """Активация пользователя (только для суперпользователей)"""
    user = activate_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
