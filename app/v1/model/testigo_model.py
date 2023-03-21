import peewee

from app.v1.utils.db import db
from persona_model import Persona
from juicio_model import Juicio

class Testigo(peewee.Model):
    testigo = peewee.ForeignKeyField(Persona)
    juicio = peewee.ForeignKeyField(Juicio)
    notificacion = peewee.CharField()
    audiencia = peewee.CharField()

    class Meta:
        database = db