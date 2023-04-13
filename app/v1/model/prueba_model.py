import peewee

from app.v1.utils.db import db
from .persona_model import Persona
from .juicio_model import Juicio

class Prueba(peewee.Model):
    juicio = peewee.ForeignKeyField(Juicio)
    perito = peewee.ForeignKeyField(Persona)
    tipo = peewee.CharField()
    estado_asignacion = peewee.CharField()
    estado_aceptacion = peewee.CharField()
    fecha_aceptacion = peewee.DateField()
    estado_presentacion = peewee.CharField()
    vencimiento_presentacion = peewee.DateField()
    estado_pericia = peewee.CharField()
    porc_pericia = peewee.FloatField()
    valor_tratamiento = peewee.FloatField()
    valor_reparacion = peewee.FloatField()
    valor_desvalorizacion = peewee.FloatField()
    privacion_uso = peewee.IntegerField()
    resultado = peewee.CharField()
    observaciones = peewee.TextField()
    destinatario = peewee.CharField()
    fecha_presentacion = peewee.DateField()
    fecha_contestacion = peewee.DateField()
    
    class Meta:
        database = db