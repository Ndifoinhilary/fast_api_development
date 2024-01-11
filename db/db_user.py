from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DbUser

from schemes import UserBase


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# to retrieve all users of the systems
def get_all_user(db: Session):
    return db.query(DbUser).all()


# getting s single user
def get_single_user(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()


# update a user in the db


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    user.update(
        {
            DbUser.username: request.username,
            DbUser.email: request.email,
            DbUser.password: Hash.bcrypt(request.password),
        }
    )
    db.commit()
    return "OK"


# delete a user


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return "Ok"
