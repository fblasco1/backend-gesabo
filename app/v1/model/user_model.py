import peewee

from app.v1.utils.db import db

class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    usuario = peewee.CharField(unique=True, index=True)
    contraseña = peewee.CharField()
    tipo = peewee.CharField()

    class Meta:
        database = db