from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from fastapi.security import OAuth2PasswordRequestForm

from app.v1.schema import user_schema
from app.v1.service import user_service
from app.v1.service import auth_service
from app.v1.schema.token_schema import Token

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1", tags=["users"])

@router.post(
    "/user/",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo usuario"
)
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Crea un nuevo usuario en la app

    ### Param
    La app recive los siguientes campos en formato JSON
    - email: Un email válido
    - usuario: Un nombre de usuario único
    - contrasenia: Una contraseña que cumpla con las normas de seguridad

    ### Retorna
    - user: La información del usuario creado 
    """
    return user_service.create_user(user)

@router.post(
    "/login",
    response_model=Token
)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    ## Login con Token

    ### Params
    La app recibe de un formulario los siguientes campos
    - username: Tu nombre de usuario o email
    - password: Tu contrasenia

    ### Retorna
    - Un token de acceso y el tipo de token
    """
    access_token = auth_service.generate_token(form_data.username, form_data.password)
    return Token(access_token=access_token, token_type="bearer")