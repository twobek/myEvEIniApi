from sqlalchemy import Column, Integer, Date, Text, String

from src import db
class Param(db.Model):
    __tablename__ = 'param'
    type = Column(String, primary_key=True)
    date = Column(Date)
    text = Column(Text)
    number = Column(Integer)