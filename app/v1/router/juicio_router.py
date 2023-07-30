from fastapi import status, APIRouter, Depends, Body
from typing import List

from app.v1.schema import juicio_schema
from app.v1.service import juicio_service, auth_service
from app.v1.utils.db import get_db

router = APIRouter(
    prefix="/api/v1/juicio",
    dependencies=[Depends(auth_service.get_current_user)]
)

@router.post(
    "/",
    tags=["juicio"],
    status_code=status.HTTP_201_CREATED,
    response_model=juicio_schema.Juicio,
    dependencies=[Depends(get_db)]
)
def create_juicio(
    juicio: juicio_schema.JuicioCreate = Body(...),
    ):
    juicio_creado = juicio_service.create_juicio(juicio)
    return juicio_creado

@router.get(
    "/",
    tags=["juicio"],
    status_code=status.HTTP_200_OK,
    response_model=List[juicio_schema.Juicio],
    dependencies=[Depends(get_db)]
)
def get_juicios():
    return juicio_service.get_juicios()