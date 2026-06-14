from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


# ── Engine cache — one engine per DB name, reused across calls ────────────────
_engines = {}

def _get_engine(db_name: str):
    if db_name not in _engines:
        DATABASE_URL = f"mysql+pymysql://root:@localhost/{db_name}"
        _engines[db_name] = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,       # test connection before using it
            pool_recycle=280,         # recycle connections every ~4.5 min
            pool_size=5,
            max_overflow=10,
        )
    return _engines[db_name]


def get_db_connection(db_name: str) -> Session:
    """Returns a brand-new session each time. Caller is responsible for closing."""
    engine = _get_engine(db_name)
    SessionLocal = sessionmaker(bind=engine)
    return SessionLocal()


def get_session_factory(db_name: str):
    """Returns a factory you can call to get a fresh session whenever needed."""
    engine = _get_engine(db_name)
    return sessionmaker(bind=engine)


from models import src_models
from sqlalchemy import text

if __name__ == "__main__":
    db = get_db_connection("orderTracking")
    result = db.query(src_models.Order).all()
    for row in result:
        print(row.orderNumber)
    db.close()