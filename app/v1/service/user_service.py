from fastapi import HTTPException, status

from app.v1.model.user_model import User as UserModel
from app.v1.schema import user_schema
from app.v1.service.auth_service import get_password_hash

def create_user(user: user_schema.UserRegister):

    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.usuario == user.usuario)).first()
    if get_user:
        msg = "Ese email ya fue registrado"
        if get_user.usuario == user.usuario:
            msg = "Ese nombre de usuario ya fue registrado"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        usuario=user.usuario,
        email=user.email,
        contrasenia=get_password_hash(user.contrasenia),
        tipo="abogado"
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        usuario = db_user.usuario,
        email = db_user.email,
        tipo = db_user.tipo
    )

def create_superuser(user: user_schema.UserRegister):

    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.usuario == user.usuario)).first()
    if get_user:
        msg = "Ese email ya fue registrado"
        if get_user.usuario == user.usuario:
            msg = "Ese nombre de usuario ya fue registrado"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        usuario=user.usuario,
        email=user.email,
        contrasenia=get_password_hash(user.contrasenia),
        tipo="admin"
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        usuario = db_user.usuario,
        email = db_user.email,
        tipo = db_user.tipo
    )