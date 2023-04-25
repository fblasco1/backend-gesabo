import peewee

from app.v1.utils.db import db
from .jurisdiccion_model import Jurisdiccion
from .user_model import User

class Juicio(peewee.Model):
    jurisdicion = peewee.ForeignKeyField(Jurisdiccion)
    caratula = peewee.CharField()
    nexpediente = peewee.CharField()
    materia = peewee.CharField()
    estado_procesal = peewee.CharField()
    situacion_tramite = peewee.CharField()
    tipo_reclamo = peewee.CharField()
    siniestro = peewee.IntegerField()
    poliza = peewee.IntegerField()
    suma_asegurada = peewee.FloatField()
    monto_demanda = peewee.FloatField()
    fecha_hecho = peewee.DateField()
    fecha_notificacion = peewee.DateField()
    fecha_contestacion = peewee.DateField()
    fecha_mora = peewee.DateField()
    hechos_demanda = peewee.TextField()
    hechos_contestacion = peewee.TextField()
    evaluacion = peewee.CharField()
    transabilidad = peewee.BooleanField()
    defensas_opuestas = peewee.CharField()
    observaciones = peewee.TextField()
    informe_medico = peewee.FloatField()

    class Meta:
        database = db

class Juicio_Abogado(peewee.Model):
    abogado = peewee.ForeignKeyField(User, backref="abogados")
    juicio = peewee.ForeignKeyField(Juicio, backref="juicios")

    class Meta:
        database = db