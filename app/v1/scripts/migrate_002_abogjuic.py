from playhouse.migrate import *

from app.v1.utils.db import db
from app.v1.model.juicio_model import Juicio_Abogado

def migrate_002_abogjuic():
    migrator = PostgresqlMigrator(db)

    migrate(
        migrator.drop_column('juicio', 'responsable_id'),
    )

    db.create_tables([Juicio_Abogado])