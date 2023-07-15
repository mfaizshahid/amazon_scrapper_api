from app.config.db import local_session


def get_db_session():
    db = local_session()
    try:
        yield db
    finally:
        db.close()
