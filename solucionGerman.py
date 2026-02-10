def area_rectangulo(largo, ancho):
    return largo * ancho


def perimetro_rectangulo(largo, ancho):
    return 2 * (largo + ancho)


largo = 10
ancho = 5

print(f"Área: {area_rectangulo(largo, ancho)}")
print(f"Perímetro: {perimetro_rectangulo(largo, ancho)}")
