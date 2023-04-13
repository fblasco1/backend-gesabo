import peewee
from contextvars import ContextVar
from fastapi import Depends


from app.v1.utils.settings import Settings

SETTINGS = Settings()

POSTGRES_USER = SETTINGS.POSTGRES_USER
POSTGRES_PASSWORD = SETTINGS.POSTGRES_PASSWORD
POSTGRES_SERVER = SETTINGS.POSTGRES_SERVER
POSTGRES_PORT = SETTINGS.POSTGRES_PORT
POSTGRES_DB = SETTINGS.POSTGRES_DB

db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())

class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.PostgresqlDatabase(POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host=POSTGRES_SERVER, port=POSTGRES_PORT)

db._state = PeeweeConnectionState()

async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()