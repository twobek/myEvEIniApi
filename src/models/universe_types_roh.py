from sqlalchemy import Column, Integer, DateTime

from src import db
class UniverseTypesROH(db.Model):
    __tablename__ = 'universe_types_roh'
    type_id = Column(Integer, primary_key=True)
    creation_ts = Column(DateTime)

