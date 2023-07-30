from sqlmodel import SQLModel, create_engine  

from .settings import Settings

settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_password
DB_HOST = settings.db_host
DB_PORT = settings.db_port

postgres_url = "postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
engine = create_engine(postgres_url)