import peewee

from app.v1.utils.db import db
from juicio_model import Juicio

class Transaccion(peewee.Model):
    juicio = peewee.ForeignKeyField(Juicio)
    resultado = peewee.CharField()
    capital_ofrecido = peewee.FloatField()
    capital_pretendido = peewee.FloatField()
    fecha_ingreso = peewee.DateField()
    observacion = peewee.TextField()

    class Meta:
        database = db