import peewee 

from app.v1.utils.db import db
from juzgado_model import Juzgado

class Secretaria(peewee.Model):
    juzgado = peewee.ForeignKeyField(Juzgado)
    secretario = peewee.CharField()
    email = peewee.CharField(unique=True, index=True)

    class Meta:
        database = db