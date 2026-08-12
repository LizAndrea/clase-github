
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
    rows = ["Ironman", "Batman", "Jocker", "spiderman", "antman ", "thor", "lucky"]
    return rows

#Crear endpoints con su nombre y que contiene (enfocado a el taller)

@app.get("/carlos")
def get_estructuras_datos():
    rows = ["Pilas", "Colas", "Array", "Mapas", "Diccionario", "Arboles", "Grafos"]
    return rows