import peewee

from app.v1.utils.db import db

class Jurisdiccion(peewee.Model):
    provincia = peewee.CharField()
    sede = peewee.CharField()

    class Meta:
        database = db