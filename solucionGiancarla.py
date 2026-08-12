def calcularArea(largo, ancho):
    return largo * ancho

def calcularPerimetro(largo, ancho):
    return 2 * (largo + ancho)

largo, ancho = 10, 5

print(f"Área: {calcularArea(largo, ancho)}")
print(f"Perímetro: {calcularPerimetro(largo, ancho)}")