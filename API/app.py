
import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Andrea", "Marce", "Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

@app.get("/andreaTaller")
def get_superheroes():
    rows = ["Superman", "Desarrollo", "FastAPi", "control de versiones", "refactorizacion", "SOLID ", "GIT", "inteligencia Artifical"]
    return rows

#Crear endpoints con su nombre y que contiene (enfocado a el taller)
@app.get("/douglasTaller")
def get_superheroes():
    rows = ["Programacion", "Api", "Base de datos", "SOLID", "Postgres"]
    return rows