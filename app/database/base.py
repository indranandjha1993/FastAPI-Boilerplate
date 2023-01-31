from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import settings

Base = declarative_base()
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=False)
