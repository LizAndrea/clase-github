#codigo fuente
def HallarArea(base, altura)
    return base * altura

def HallarPerimetro(base, altura)
    return 2 * (base + altura)

base = 10
altura = 5

area = HallarArea(base, altura)
perimetro = HallarPerimetro(base, altura)

print(f"Area: {area}")
print(f"Perimetros: {perimetro}")