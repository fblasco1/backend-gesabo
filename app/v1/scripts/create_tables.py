from app.v1.model import user_model, jurisdiccion_model,fuero_model,juzgado_model,secretaria_model,juicio_model,persona_model,prueba_model,testigo_model,transaccion_model

from app.v1.utils.db import engine, SQLModel

SQLModel.metadata.create_all(engine)