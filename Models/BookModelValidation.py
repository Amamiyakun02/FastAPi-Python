from pydantic import BaseModel


class BookValidation(BaseModel):
    id: int
    name: str
    pengarang: str
    id_penerbit: int