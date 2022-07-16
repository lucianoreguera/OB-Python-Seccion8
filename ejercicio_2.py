class Vehiculo:
    def __init__(self, marca: str, color: str, precio: float):
        self.marca = marca
        self.color = color
        self.precio = precio

    def __str__(self):
        return f'Marca: {self.marca} - Color: {self.precio} - Precio: ${self.precio}'


auto = Vehiculo('Nissan', 'Versa', 20000)

file = open('lista_vehiculos.txt', 'w')
file.write(auto.__str__())
file.close()

file = open('lista_vehiculos.txt', 'r')

for line in file.readlines():
    print(line)

file.close()
