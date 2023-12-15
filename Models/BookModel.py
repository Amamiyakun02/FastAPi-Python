
from db_config import Base
from sqlalchemy import Column, Integer, String

class Book(Base):

    __tablename__ = 'book'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255), nullable=False)
    pengarang = Column('pengarang', String(255), nullable=False)
    id_penerbit = Column('id_penerbit', Integer, nullable=False)

