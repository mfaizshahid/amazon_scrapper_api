from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
load_dotenv()
DB_URL = URL.create(
    drivername=os.environ.get("db_drivername"),
    database=os.environ.get("database"),
    host=os.environ.get("db_host"),
    username=os.environ.get("db_username"),
    password=os.environ.get("db_pass"),
)
engine = create_engine(DB_URL)


local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)
