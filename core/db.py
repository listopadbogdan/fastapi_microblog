from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from environs import Env

env = Env()
env.read_env()

DATABASE_URL = env('SQLALCHEMY_DATABASE_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
engine.begin()
Base = declarative_base()



