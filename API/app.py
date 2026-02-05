
import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Andrea", "Marce", "Miranda"]
    return rows


@app.get("/taller")
def get_superheroes():
    rows = ["Desarrollo", "FastAPi", "control de versiones", "refactorizacion", "SOLID ", "GIT", "inteligencia Artifical"]
    return rows

#Crear endpoints con su nombre y que contiene (enfocado a el taller)