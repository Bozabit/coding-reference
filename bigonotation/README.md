# Big O Notation

## What is Big O
- Mathematical Notation
Es la forma de calcular el impacto que tiene un algoritmo cuando se usa una sola vez o un millón de veces. Es decir calcular el costo de un algoritmo

### O(1)
Tiempo constante, es decir no importa cuan largo sea el input de la función, siempre corre de forma constante. 0(1) = tiempo constante.

### O(n)
Es cuando una funcion es lineal. Aumenta de form directamente proporcional al tamaño del input

### 0(n<sup>2</sup>)
Es cuando el tiempo de una función es descrita por una línea cuadrática. Y quizas una de las peores soluciones.

### O(log n)
Es el tipo de algoritmo que resulta mas eficiente, y es representado por una curva logaritmica. Ocurre cuando reducimos la cantidad de trabajo por mitades en cada paso del proceso de búsqueda

### O(2<sup>n</sup>)
El peor tipo de funciones, pues decribe una curva exponecial que aumenta el doble de tiempo por cada paso.

### Space Complexity vs Runtime Complexity (Time)
Es la misma nomenclatura de Big O Notation, pero cuando se refiere a espacio en memoria. Siempre se enfoca en calcular que tanto espacio debemos usar para esa función. Por ejemplo si tengo un array X y entonces como primer paso de la funcion lo copio para hacer actividades, tengo una funcion de 0(n) space, pues estaria siempre duplicando el espacio que ocupa el input

# Estructura de Datos

## Arrays
### Overview
Es una lista de elementos. Que son guardados de forma secuencial en la memoria del sistema. Según Big O Notation tienen un peso de 0(1)

Si uno necesita una lista de elementos y accesarlos por el index de cada uno de elolos, son sin duda el mejor esquema de datos.

El mayor problema que tienen es que son de tamño fijo

