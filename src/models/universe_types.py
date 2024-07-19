from sqlalchemy import Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from src import db
class UniverseTypesROH(db):
    __tablename__ = 'universe_types_roh'
    type_id = Column(Integer, primary_key=True)
    creation_ts = Column(Date)
    api_page = Column(Integer)
