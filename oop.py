# Programacion Orientada a Objetos (OOP = Object Oriented Programming) en Python
""" 
OOP
 
se base en:
1. Clases -> plantilla
2. Objetos -> Instancia de las clases

"""

class Persona: # Plantilla
    pass


persona1 = Persona() # Instancia



# Ejemplo:

class Persona:
    def __init__(self):
        self.nombre = "John" # Atributo
        self.apellido = "Doe" # Atributo
        self.edad = "1000" # Atributo
        self.direccion = "La Luna" # Atributo
        
    def hablar(self): # Método
        pass
    
    def caminar(self): # Método
        pass
    
    def saludar(self): # Método
        print(f"Hola, soy {self.nombre}")
        

p = Persona()
p.saludar() # Hola, soy John


j = Persona()
j.nombre = "Jerimar"
j.apellido = "Perez"

j.saludar() # Hola, soy Jerimar

# Conceptos Claves de la OOP

# 1. Encapsulamiento: Agrupar datos y compotamientos dentro de una clase

class Cuenta:
    def __init__(self, saldo = 0):
        self.saldo = saldo
        
    def depositar(self, monto):
        self.saldo += monto
        
c = Cuenta(1000) # Instancia => __init__()
c.depositar(2000) # Incrementamos el saldo


# 2. Abstraccion: Ocultar la complejidad y mostrar solo lo necesario

class Auto:
    def encender(self):
        print("Auto encendido!")
        
# 3. Herencia

class Animal:
    def __init__(self, raza):
        self.raza = raza
        
    def hablar(self):
        print("Emitir un sonido")
        
class Perro(Animal):
    def hablar(self):
        print("Ladrar")
        
class Gato(Animal):
    def hablar(self):
        print("Maullar")

p = Perro()
p.hablar()

g = Gato()
g.hablar()

# 4. Polimorfismo: Un mismo metodo tendra un comportamiento distinto segun el objeto

animales = [Perro(), Gato()] # [<Perro />, <Gato />]

for animal in animales:
    animal.hablar()
    
# Atributos Privados (convención)

class Usuario:
    def __init__(self):
        self.nombre = "John" # Público
        self._nombre = "John" # Protegido
        self.__nombre = "John" # Privado
        
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre