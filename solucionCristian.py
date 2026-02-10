base = 10
altura = 5

def calcular_area(base, altura):
    return base * altura

def calcular_perimetro(base, altura):
    return 2 * (base + altura)

# Calcular y mostrar resultados
area = calcular_area(base, altura)
perimetro = calcular_perimetro(base, altura)

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")