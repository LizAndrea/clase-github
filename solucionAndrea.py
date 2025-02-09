def getArea(length, width):
    return f'Area: {length * width}'

def getPerimeter(length, width):
    return f'Perimeter: {2 * (length + width)}'

length = 10
width = 5

print(getArea(length, width))
print(getPerimeter(length, width))
