import peewee

from app.v1.utils.db import db

class Persona(peewee.Model):
    cuit = peewee.IntegerField()
    tipo = peewee.CharField()
    rol = peewee.CharField()
    nombre = peewee.CharField()
    razon_social = peewee.CharField()
    domicilio = peewee.CharField()
    telefono = peewee.IntegerField()
    email = peewee.CharField(unique=True, index=True)
    fecha_nacimiento = peewee.DateField()

    class Meta: 
        database = db