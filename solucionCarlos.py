# Funcion para calcular el area de un rectangulo
def calcular_area_rectangulo(largo, ancho):
  return largo * ancho

# Funcion para calcular el perimetro de un rectangulo
def calcular_perimetro_rectangulo(largo, ancho):
  return 2 * (largo + ancho)

print("Area: ", calcular_area_rectangulo(10, 5))
print("Perimetro: ", calcular_perimetro_rectangulo(10, 5))