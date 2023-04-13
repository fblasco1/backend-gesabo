import peewee

from app.v1.utils.db import db
from .fuero_model import Fuero

class Juzgado(peewee.Model):
    fuero = peewee.ForeignKeyField(Fuero)
    numero = peewee.IntegerField()
    nombre = peewee.CharField()
    domicilio = peewee.CharField()
    telefono = peewee.IntegerField()
    email = peewee.CharField(unique=True, index=True)
    juez = peewee.CharField()
    
    class Meta:
        database = db