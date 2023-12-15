from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
db_url = "mariadb+mysqlconnector://amamiya:amamiyakun02@localhost/fastapi"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
# try:      
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     # Coba membuat sesi (koneksi)
#     session = SessionLocal()
#      # Tutup sesi setelah mencobanya
#
#     print("Koneksi ke database berhasil!")
#
# except Exception as e:
#     print(f"Terjadi kesalahan saat mencoba koneksi ke database: {str(e)}")


Base = declarative_base()
# class Book(Base):
#
#     __tablename__ = 'book'
#     id = Column('id', Integer, primary_key=True)
#     name = Column('name', String(255), nullable=False)
#     pengarang = Column('pengarang', String(255), nullable=False)
#     id_penerbit = Column('id_penerbit', Integer, nullable=False)

#
# try:
    # Mengambil data dari tabel "user"
#     books = session.query(Book).all()
#
#     # Menampilkan hasil
#     for book in books:
#         print(f"ID: {book.id}, name: {book.name}, pengarang: {book.pengarang}, id_penerbit: {book.id_penerbit}")
#
# except Exception as e:
#     print(f"Terjadi kesalahan: {str(e)}")
#
# finally:
#     session.close()
