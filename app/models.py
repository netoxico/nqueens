from datetime import datetime
from sqlalchemy import Column, Sequence, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import postgresql

Base = declarative_base()


class Result(Base):
    __tablename__ = 'result'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    n = Column(Integer)
    result = Column(postgresql.ARRAY(Integer, dimensions=1))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return "<Result('%s')>" % (self.id)
