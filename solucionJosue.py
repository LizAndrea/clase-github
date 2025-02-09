def calcular_area(base, altura):
    #calculo del area
    return base * altura

def calcular_perimetro(base, altura):
    #calculoPerimetro
    return 2 * calcular_area(base, altura)

# Definicion de variables: base, altura
base = 10
altura = 5

# Calcular y mostrar resultados
area = calcular_area(base, altura)
perimetro = calcular_perimetro(base, altura)

print(f"Área: {area} de \nPerímetro: {perimetro}")