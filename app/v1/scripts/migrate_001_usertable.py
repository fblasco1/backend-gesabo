from app.v1.utils.db import db
from playhouse.migrate import *

def migrate_001_user():
    migrator = PostgresqlMigrator(db)

    migrate(
        migrator.rename_column('user', 'contraseña', 'contrasenia'),
    )