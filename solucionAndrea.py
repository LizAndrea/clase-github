class Rectangulo:
    """Clase para representar un rectángulo y calcular su área y perímetro."""

    def __init__(self, base, altura):
        """Inicializa las dimensiones del rectángulo."""
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Calcula el área del rectángulo."""
        return self.base * self.altura

    def calcular_perimetro(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.base + self.altura)

    def mostrar_resultados(self):
        """Muestra el área y el perímetro del rectángulo."""
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f"Área: {area}")
        print(f"Perímetro: {perimetro}")


rectangulo = Rectangulo(base=10, altura=5)

rectangulo.mostrar_resultados()
