
from fastapi import FastAPI, status
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





