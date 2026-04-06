# Funciones

"""  

def nombre_funcion(params):
    codigo
    
    
nombre_funcion = lambda params : operacion 


"""

def sumar(a, b = 15):
    return a + b

restar = lambda a, b: a - b

# 1. Parametros Posicionales

resultado = sumar(10, 10)

# 2. Parametros por Defecto
resultado2 = sumar(10) # 25

# 3. Argumentos Nombrados

resultado = sumar(b=45, a=20)

# 4. *args (Argumentos Variables)

def sumar(*numeros):
    return sum(numeros)

print(sumar(1, 2, 3, 4, 5, 6, 7))
print(sumar(1, 2, 3, 4))

# 5. **kargs (Argumentos Clave-Valor)

def mostrar_datos(**datos):
    print(f"Hola mi nombre es: {datos["nombre"]} {datos["apellido"]}")
    
mostrar_datos(nombre="Luis", apellido="Rodriguez")


def ejemplo(a, b=10, *args, **kargs):
    print(a, b)
    print(args)
    print(kargs)

print("Combinado:")
ejemplo(5, 12, 4, 6, nombre="John", apellido="Doe")
    