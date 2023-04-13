import peewee

from app.v1.utils.db import db
from .jurisdiccion_model import Jurisdiccion

class Fuero(peewee.Model):
    jurisdiccion = peewee.ForeignKeyField(Jurisdiccion)
    fuero = peewee.CharField()

    class Meta:
        database = db