# Declaración de clase CircularBuffer
class CircularBuffer:

    # Inicialización de clase
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0  # Índice de la posición actual para insertar nuevos elementos
        self.is_full = False

    # Establecimiento de primer estado
    def start(self, item):
        self.buffer = [item] * self.size
        self.is_full = True
        self.head = 0

    # Ingres de información a la clase
    def insert(self, item):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.size  # Avanza al siguiente índice de forma circular

        if self.head == 0:
            self.is_full = True

    # Extracción de elementos dentro de la clase
    def get_elements(self):
        if self.is_full:
            return self.buffer[self.head:] + self.buffer[:self.head]
        else:
            return self.buffer[:self.head]

# Ejemplo de uso
buffer_size = 5
buffer = CircularBuffer(buffer_size)
buffer.start(0)

# Insertar elementos en el buffer
buffer.insert(1)
elementos = buffer.get_elements()
print(elementos)
buffer.insert(0)
elementos = buffer.get_elements()
print(elementos)
buffer.insert(1)
elementos = buffer.get_elements()
print(elementos)
buffer.insert(1)
elementos = buffer.get_elements()
print(elementos)
buffer.insert(1)
elementos = buffer.get_elements()
print(elementos)

# El buffer está lleno, se sobrescribirá el primer elemento (Dato 1) al insertar uno nuevo
buffer.insert(0)

# Obtener los elementos almacenados en el buffer
elementos = buffer.get_elements()
print(elementos)
