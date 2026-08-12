
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

@app.get("/herbert")
def get_peter_poker():
    estructuras_de_datos = ["Pilas", "Colas", "Listas", "Árboles", "Grafos"]
    return {"nombre": "Peter Poker", "alterEgo": "Spider-Ham", "Estructuras de datos": estructuras_de_datos}
  
@app.get("/giancarla")
def get_pilares_POO():
    rows = ["herencia", "abstracción", "Encapsulamiento", "polimorfismo"]
    
@app.get("/conexion_microservicios_backend")
def get_conexion_microservicios_backend():
    rows = ["Eureka", "Zuul", "Spring Cloud Config", "Hystrix", "Ribbon"]
    return rows

@app.get("/elnar")
def get_lenguajes_backend():
    rows = ["Python", "Java", "C#", "Node.js", "Ruby"]
    return rows

@app.get("/andrea")
def get_lenguajes_backend():
    rows = ["Python", "Java", "C#", "Node.js", "Ruby"]
    return rows

