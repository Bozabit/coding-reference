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

    ''' Métodos Mágicos 
    https://rszalski.github.io/magicmethods/
    '''

    # __str__ cuando convertirmo el objeto a un string
    def __str__(self):
        return f'({self.x}, {self.y})'

    # __eq__  comparando dos objetos cuando deben ser iguales
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # cuando un punto debe ser mas grande que el otro, lo cual sirve para que python entienda sin es menor que
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    ''' Métodos Aritméticos '''

    # add
    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)

    # resta
    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)


punto = Punto(1, 2)
# funcion para el tipo de objeto
print(f'Tipo de objeto {type(punto)}')
# funcion para determinar el tipo de instancia
print(f'Es instancia de Punto => {isinstance(punto,Punto)}')
# imprimiendo atributos
punto.draw()

# otro objeto de atributos particulares
punto2 = Punto(1, 2)
punto2.draw()

# puntocreado usando el metodo zero
punto3 = Punto.zero()
punto3.draw()

# chequeando cuando el punto se convierte a string
print(punto3)
# es igual?
print(f'El punto {punto} es igual al punto {punto2} {punto == punto2}')
# mayor que
print(f'El punto {punto} es mayor que el punto {punto3} {punto > punto3}')
# menor que
print(f'El punto {punto} es menor que el punto {punto3} {punto < punto3}')
# probando la suma
print(f'Sumando el punto {punto} + el punto {punto2} => {punto+punto2}')
print(f'Restando el punto {punto} - el punto {punto2} => {punto-punto2}')


''' Properties '''


class Product:
    def __init__(self, price):
        self.price = price

    # properties al estilo python
    @property
    def price(self):
        return self.__price

    # Metodos opcionales, como todo setter y getter
    @price.setter
    def price(self, value):
        if value < 0:
            # Value Error es una excepcion nativa de Python
            raise ValueError("Precio no peude ser menor que cero")
        self.__price = value


product = Product(50)
print(product.price)
