from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemes import UserBase, UserDisplay
from db import db_user

router = APIRouter(prefix="/user", tags=["user"])

# creating a user


@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# read users that's all users
@router.get("/", response_model=List[UserDisplay])
def list_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_user(db)


# getting a single user from the db
@router.get("/{id}", response_model=UserDisplay)
def get_single_user(db: Session = Depends(get_db)):
    return db_user.get_single_user(db, id)


# updating a user in the db


@router.post("/{id}/update")
def update_user(request: UserBase, id: int, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)


# deleting a user from the db


@router.get("/{id}/delete")
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)
