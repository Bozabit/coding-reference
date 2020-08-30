''' Arrays operations ni Python '''
''' Se usan los arrays para sustituir listas que tengan un mal performance '''

from array import array
numbers = array('b', [1, 2, 3])
numbers.append(4)
numbers.insert(2, 5)
numbers.remove(4)
print(numbers)
