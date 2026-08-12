def calcular_area(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def calcular_perimetro(base, altura):
    """Calcula el perímetro de un rectángulo."""
    return 2 * (base + altura)

# Definir dimensiones del rectángulo
base = 10
altura = 5

# Calcular y mostrar resultados
area = calcular_area(base, altura)
perimetro = calcular_perimetro(base, altura)

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")