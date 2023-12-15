from db_config import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'user'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(255), nullable=False)
    firstname = Column('firstname', String(255), nullable=False)
    lastname = Column('lastname', String(255), nullable=False)