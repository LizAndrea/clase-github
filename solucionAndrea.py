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


####################################################################################################
#########################################Rodrigo####################################################
def calcular_area(base, altura):
    """Calcula el área de un rectángulo."""
    if base <= 0 or altura <= 0: 
        raise ValueError("Base y altura deben ser mayores que 0.")
    return base * altura

def calcular_perimetro(base, altura):
    """Calcula el perímetro de un rectángulo."""
    if base <= 0 or altura <= 0: 
        raise ValueError("Base y altura deben ser mayores que 0.")
    return 2 * (base + altura)

def mostrar_resultados(base, altura):
    try:
        print(f"Área: {calcular_area(base, altura)}")
        print(f"Perímetro: {calcular_perimetro(base, altura)}")
    except ValueError as e:
        print(f"Error: {e}")

# Ejemplo de uso
base, altura = 10, 5
mostrar_resultados(base, altura)
