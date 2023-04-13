from app.v1.model.user_model import User
from app.v1.model.jurisdiccion_model import Jurisdiccion
from app.v1.model.fuero_model import Fuero
from app.v1.model.juzgado_model import Juzgado
from app.v1.model.secretaria_model import Secretaria
from app.v1.model.juicio_model import Juicio
from app.v1.model.persona_model import Persona
from app.v1.model.prueba_model import Prueba
from app.v1.model.testigo_model import Testigo
from app.v1.model.transaccion_model import Transaccion

from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([User, Jurisdiccion, Fuero, Juzgado, Secretaria, Juicio, Persona, Prueba, Testigo, Transaccion])
