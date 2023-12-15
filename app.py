from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from typing import Optional
from Models.FoodModel import FoodName

from db_config import session


# import model database
from Models.BookModelValidation import BookValidation
from Models.userModel import User
from Models.BookModel import Book
app = FastAPI()

# Konfigurasi CORS agar frontend dapat berkomunikasi dengan backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Contoh data
data = {
    "nama": "Abidin",
    "alamat": "Tambang Ulang RT.02 RW.01",
    "usia": 21,
    "nama_panggilan": "Abidn"
}

class DataResponse(BaseModel):
    nama: str
    alamat: str
    usia: int
    nama_panggilan: str

@app.get("/bio", response_model=DataResponse)
async def get_data():
    return data

# model langsung dari database
class UserData(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str

class BookData(BaseModel):
    id: int
    nama: str
    pengarang: str
    idPenerbit: int

class UserResponse(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str

class DataResponse2(BaseModel):
    user: UserData
    book: BookData


user = session.query(User).filter_by(id=3).first()
book = session.query(Book).filter_by(id=1).first()
# Menampilkan hasil
Userdata = {
    "user": {
        "id": user.id,
        "username": user.username,
        "firstname": user.firstname,
        "lastname": user.lastname,
    },
    "book": {
        "id": book.id,
        "nama": book.name,
        "pengarang": book.pengarang,
        "idPenerbit": book.id_penerbit
    }
}

@app.get("/data_user")
async def get_Data2():
    # UserDataAll = session.query(User).all()
    return Userdata


@app.get("/get_user_by_id/{user_id}", response_model=UserResponse)
async def get_by_id(user_id: int):
    userdata = session.query(User).filter_by(id=user_id).first()
    return userdata

@app.get("/items/{item_id}")
async def read_item(item_id: int, da: str | None = None):
    return {"item_id": item_id, "q": da}

@app.get("/food/{food_name}")
async def get_food(food_name: FoodName):
    if food_name == FoodName.sayur:
        return {"food_name": food_name, "msg": "kamu memasukan tipe sayur"}
    if food_name == FoodName.buah:
        return {"food_name": food_name, "msg": "kamu memasukkan tipe buah"}
    if food_name == FoodName.makanan:
        return {"food_name": food_name, "msg": "kamu memasukkan makanan"}


@app.post("/book")
async def create_book(book: BookValidation):
    return book