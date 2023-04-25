from datetime import date

from pydantic import BaseModel
from pydantic import Field
from app.v1.schema.jurisdiccion_schema import Jurisdiccion
from app.v1.schema.user_schema import User

class JuicioCreate(BaseModel):
    juris_id: int = Field(...)
    abogados: list[int] | int = Field(...)
    caratula : str = Field(
        ...,
        max_length=150,
        example="PEREZ JULIO C/ GARCIA LUIS Y OTROS"
    )
    nexpediente: str = Field(
        ...,
        example="44031/2017"
    )
    materia: str = Field(
        ...,
        example="AUTOS"
    )
    estado_procesal: str = Field(
        ...,
        example="Prueba",
        max_length=30
    )
    situacion_tramite: str = Field(
        ...,
        example="TRAMITE",
        max_length=10
    )
    tipo_reclamo: str = Field(
        ...,
        example="CONTRACTUAL",
        max_length=30
    )
    siniestro: int | None = Field(
        default=None
    )
    poliza: int | None = Field(
        default=None
    )
    suma_asegurada: float | None = Field(
        default=None
    )
    monto_demanda: float | None = Field(
        default=None
    )
    fecha_hecho: date = Field(
        example="DD/MM/AAAA"
    )
    fecha_notificacion: date = Field(
        example="DD/MM/AAAA"
    )
    fecha_contestacion: date = Field(
        example="DD/MM/AAAA"
    )
    fecha_mora: date = Field(
        example="DD/MM/AAAA"
    )
    hechos_demanda: str = Field(
        max_length=500,
        example= "El actor conducía su motocicleta en Güemes, ciudad Evita cuando al llegar a una rotonda ingresa a la misma y es embestido por el demandado en su parte lateral derecha de la motocicleta"
    )
    hechos_contestacion: str = Field(
        max_length=500,
        example="El actor conducía su motocicleta en Güemes, ciudad Evita cuando al llegar a una rotonda ingresa a la misma y es embestido por el demandado en su parte lateral derecha de la motocicleta"
    )
    evaluacion: str = Field(
        example="B0 - TRANSABLE - CULPA EXCLUSIVA O CONC. CON 3° INSOLVENTE"
    )
    transabilidad: bool = Field()
    defensas_opuestas: str | None = Field(
        default=None,
        max_length=100,
        example="NEGATIVAS GENERICAS - IMPUGNACIÓN DE RUBROS"
    )
    observaciones: str | None = Field(
        default=None,
        max_length=255,
        example="LA CAUSA PENAL ES DESFAVORABLE - EL CONDUCTOR ASEGURADO FUE PROCESADO - PARA REVISAR EN INEBA EL dd/mm/aaaa"
    )
    informe_medico: float = Field(
    )

class Juicio(BaseModel):
    id: int = Field(...)
    caratula : str = Field(
        ...,
        max_length=150,
        example="PEREZ JULIO C/ GARCIA LUIS Y OTROS"
    )
    nexpediente: str = Field(
        ...,
        example="44031/2017"
    )
    materia: str = Field(
        ...,
        example="AUTOS"
    )
    estado_procesal: str = Field(
        ...,
        example="Prueba",
        max_length=30
    )
    situacion_tramite: str = Field(
        ...,
        example="TRAMITE",
        max_length=10
    )
    tipo_reclamo: str = Field(
        ...,
        example="CONTRACTUAL",
        max_length=30
    )
    siniestro: int | None = Field(
        default=None
    )
    poliza: int | None = Field(
        default=None
    )
    suma_asegurada: float | None = Field(
        default=None
    )
    monto_demanda: float | None = Field(
        default=None
    )
    fecha_hecho: date = Field(
        example="DD/MM/AAAA"
    )
    fecha_notificacion: date = Field(
        example="DD/MM/AAAA"
    )
    fecha_contestacion: date = Field(
        example="DD/MM/AAAA"
    )
    fecha_mora: date = Field(
        example="DD/MM/AAAA"
    )
    hechos_demanda: str = Field(
        max_length=500,
        example= "El actor conducía su motocicleta en Güemes, ciudad Evita cuando al llegar a una rotonda ingresa a la misma y es embestido por el demandado en su parte lateral derecha de la motocicleta"
    )
    hechos_contestacion: str = Field(
        max_length=500,
        example="El actor conducía su motocicleta en Güemes, ciudad Evita cuando al llegar a una rotonda ingresa a la misma y es embestido por el demandado en su parte lateral derecha de la motocicleta"
    )
    evaluacion: str = Field(
        example="B0 - TRANSABLE - CULPA EXCLUSIVA O CONC. CON 3° INSOLVENTE"
    )
    transabilidad: bool = Field()
    defensas_opuestas: str | None = Field(
        default=None,
        max_length=100,
        example="NEGATIVAS GENERICAS - IMPUGNACIÓN DE RUBROS"
    )
    observaciones: str | None = Field(
        default=None,
        max_length=255,
        example="LA CAUSA PENAL ES DESFAVORABLE - EL CONDUCTOR ASEGURADO FUE PROCESADO - PARA REVISAR EN INEBA EL dd/mm/aaaa"
    )
    informe_medico: float = Field()
    jurisdicion: Jurisdiccion = Field(...)
    abogados: list[User] | User = Field(...)