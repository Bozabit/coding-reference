''' Lists: 
Son la estructura de datos fundamental, 
de casi todo lenguaje, en algunos es conocido como arrays, 
pero en python se le llaman lists, 
los arrays son una clase que debe ser importada 
para cuando haya problemas de performance con los lists
'''

''' List creation '''
letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 100
combined = zeros + letters
numbers = list(range(21))
chars = list("Hello World")
print('Se puede crear una lista a partir de un string')
print(chars)


print(" ")
print("=" * 20)
print("Accediendo los elementos de una lista")
print("=" * 20)

''' List operations '''
print(f'Si tenemos una lista de 20 números => {letters}')
# Buscar un item específico
print(f'Buscar un item especifico ej: el tercero => {letters[2]}')
# Buscar el último item de la lista
print(f'Buscar el último item {letters[-1]}')
# Pued buscar un rango de valores en el indice
print(f'Buscar un rango 3 primeros => {letters[0:3]}')
print(f'Buscar un rango 3 primeros si el 0 => {letters[:3]}')
print(f'Buscar un rango desde el tercero en adelante => {letters[2:]}')
print(f'Mostrar todos los valores => {letters[:]}')
print(f'Mostrar cada dos elementos => {numbers[::2]}')
print(f'Mostrar cada tres elementos => {numbers[::3]}')
print(f'Mostrar en orden inverso => {letters[::-1]}')
# Saber cual es la longitud de una lista
print(f'Para la longitud se usa len() => {len(letters)}')

''' Accessing Items in a List '''
print(" ")
print("=" * 20)
print("Unpacking lists")
print("=" * 20)
# Asignar Variables de una lista a variables, debe coincidir el numero total
uno, dos, tres, cuatro = letters
print(f'Primera variable de la lista letters => {uno}')
print(f'Segunda variable de la lista letters => {dos}')
print(f'Tercera variable de la lista letters => {tres}')
print(f'Cuarta variable de la lista letters => {cuatro}')
# tomar las primeras dos variables y usar los otros
uno, dos, *otros = numbers
print(f'Primera variable de la lista numbers => {uno}')
print(f'Segunda variable de la lista numbers => {dos}')
print(f'Todos los demas => {otros}')
# tomar el primero y el ultimo
uno, *otros, ultimo = numbers
print(f'Primera variable de la lista numbers => {uno}')
print(f'Último valor de la lista => {ultimo}')
print(f'Todos los del medio => {otros}')

''' Looping Over Lists '''
print(" ")
print("=" * 20)
print("Recorreiendo las listas")
print("=" * 20)

# For loop
for letter in letters:
    print(f'Letras en la lista usando un for {letter}')

# For loop con el index con unpacking
for index, letter in enumerate(letters):
    print(f'Looping con index, letra {index} => {letter}')


''' Adding or Removing items '''
print(" ")
print("=" * 20)
print("Agregando o Removiendo Elementos")
print("=" * 20)

# Adding at the end on the list
letters.append("e")
print(f'Agregamos una letra al final de letters => {letters}')
# agregar un elemento en un lugar especifico
letters.insert(2, "-")
print(f'Agregamos - en la tercera posicion => {letters}')
# remover al final de la lista
letters.pop()
print(f'Quitamos el ultimo elemento con pop => {letters}')
# quitamos un elemento por su valor, remove solo remueve la primera ocurrencia del valor
letters.remove("b")
print(f'Quitamos la letra B (primera ocurriencia) con remove => {letters}')
# quitar elementos con del, el cual permite usar un rango
del letters[0:3]
print(f'Removimos un rango [0:3] con la función del => {letters}')
# borrar todos los elementos de la lista
letters.clear()
print(f'Borramos todo con Clear => {letters}')
# reseteo de la lista
letters = ["a", "b", "c", "d"]

''' Adding or Removing items '''
print(" ")
print("=" * 20)
print("Encontrando el indice de un elemento en una lista")
print("=" * 20)

# usando el metodo index, el cual no devuelve -1 para cuando no consigue el valor (comportammiento de Python)
print(f'Buscando un valor especifico con index() => {letters.index("c")}')

# comprobar que algo existe antes de buscar su indice
if "d" in letters:
    print(f'Buscando D solo si existe {letters.index("d")}')

# contar el numero de veces que algo sale
print(
    f'Contanto con count() las veces que sale a en {letters} => {letters.count("a")}')


''' Ordenando elementos de una lista '''
print(" ")
print("=" * 20)
print("Ordenenando Elementos en una lista")
print("=" * 20)

desorden = [3, 51, 2, 6, 8]
print(f'Una lista desordenada como {desorden}')
# utilizando el metodo sort de las listas
desorden.sort()
print(f'Ordenando la lista => {desorden}')
# indicando el reverse para invertir la lista
desorden.sort(reverse=True)
print(f'Ordenando en orden inverso => {desorden}')

# reseteando la lista
desorden = [3, 51, 2, 6, 8]
# el metodo sorted copia la lista original
print(
    f'Ordenando la lista usando el método sorted()= > {sorted(desorden)} manteniendo el orden original = > {desorden}')
# Reversar con sorted()
print(
    f'Ordenando la lista en orden reverso con sorted(reverse=True) => {sorted(desorden,reverse=True)}')

# ordenando elementos complejos como un tuple
items = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 12)
]

# usando el lambda function
''' Lambda Function: Function anonima que se pasa como argumento de otra funcion'''

items.sort(key=lambda item: item[1])
print(f'Tuples ordenados por precios usando una funcion lambda => {items}')


''' Funcion MAP '''
print(" ")
print("=" * 20)
print("Funcion map en una lista")
print("=" * 20)

precios = list(map(lambda item: item[1], items))
print(
    f'Mostrando solo los precios {precios}, sacados de una lista de tuples => {items}')


''' Funcion Filter '''
print(" ")
print("=" * 20)
print("Funcion Filter en una lista")
print("=" * 20)

filtrado = list(filter(lambda item: item[1] >= 10, items))
print(
    f'Lista filtrada con la funcion Filter() para precios mayor o igual a 10 => {filtrado} de la lista => {items}')


''' List Comprehension '''
print(" ")
print("=" * 20)
print("List Comprehension")
print("=" * 20)

# sustituto del map
precios = [item[1] for item in items]
print(
    f'Lista de precios usando List Comprehension [expression for item in items] => {precios}')

# sustituto de la funcion filter
filtrado = [item for item in items if item[1] >= 10]
print(
    f'Filtrado usando List Comprehensino [expression for item in items if item > x] => {filtrado}')

''' Funcion ZIP de las listas '''
print(" ")
print("=" * 20)
print("Función ZIP")
print("=" * 20)

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(
    f'Mezclando dos listas {list1},{list2} usando la funcion zip() => {list(zip(list1,list2))}')
