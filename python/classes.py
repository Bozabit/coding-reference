# creating classes
class Punto:
    # contructor
    def __init__(self, x, y):
        # nuevos atributos
        self.x = x
        self.y = y

    # Class level Method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # métodos, que siempre deben recibir el parametro self porque el interprete siempre lo envía
    def draw(self):
        print(f"Punto ({self.x}, {self.y})")


punto = Punto(5, 2)
# funcion para el tipo de objeto
print(f'Tipo de objeto {type(punto)}')
# funcion para determinar el tipo de instancia
print(f'Es instancia de Punto => {isinstance(punto,Punto)}')
# imprimiendo atributos
punto.draw()

# otro objeto de atributos particulares
punto2 = Punto(10, 20)
punto2.draw()

# puntocreado usando el metodo zero
punto3 = Punto.zero()
punto3.draw()
