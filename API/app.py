
import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Andrea", "Marce", "Miranda"]
    return rows


@app.get("/abdiel")
def get_lenguajes():
    rows = ["js", "python", "css", "html", "php "]
    return rows

#Crear endpoints con su nombre y que contiene (enfocado a el taller)