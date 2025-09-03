
from fastapi import FastAPI, status,HTTPException
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
app = FastAPI()


@app.get("/health")
def get_health():
    return {"message": f"OK"}



class Characteristics(BaseModel):
    ram_memory: int
    rom_memory: int

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristics

@app.post("/phones", status_code=status.HTTP_201_CREATED)
def create_phones(phones: List[Phone]):
    return {
        "message": "Phones created successfully",
        "data": phones
    } 


phones_db: List[Phone] = []





@app.get("/phones", response_model=List[Phone])
def get_phones():
    return phones_db

@app.get("/phones/{id}", response_model=Phone)
def get_phone(id: str):
    for phone in phones_db:
        if phone.identifier == id:
            return phone
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Phone with id '{id}' not found"
    )


@app.put("/phones/{id}/characteristics", response_model=Phone)
def update_characteristics(id: str, new_char: Characteristics):
    for phone in phones_db:
        if phone.identifier == id:
            phone.characteristics = new_char
            return phone
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Phone with id '{id}' not found"
    )