# Ejercicio 1
edad = int(input("Introduce tu edad: "))

if edad > 18:
    print("Es mayor de edad.")

    # Ejercicio 2
    nota = float(input("Introduce tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

    # Ejercicio 3
while True:
    try:
        numero = int(input("Ingrese un número par: "))
        if numero % 2 == 0:
            print("Ha ingresado un número par")
            break  # Salir del bucle si el número es par
        else:
            print("Por favor, ingrese un número par")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")


# Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5
contrasena = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
longitud_contrasena = len(contrasena)

if 8 <= longitud_contrasena <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# Ejercicio 6
import random
from statistics import mode, median, mean

# Definir la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular la moda, mediana y media
try:
    moda = mode(numeros_aleatorios)
except Exception:
    moda = "No hay una única moda clara"  # Manejar el caso de múltiples modas
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprimir los resultados
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Comparar la media y la mediana para determinar el sesgo
print("\nDeterminando el sesgo:")
if isinstance(moda, (int, float)):  # Verificar si hay una moda única
    if media > mediana and mediana > moda:
        print("Sesgo positivo o a la derecha.")
    elif media < mediana and mediana < moda:
        print("Sesgo negativo o a la izquierda.")
    elif media == mediana == moda:
        print("Sin sesgo.")
    else:
        print("El sesgo no se puede determinar claramente con la moda actual.")
else:
    if media > mediana:
        print("Posible sesgo positivo o a la derecha (sin una moda clara).")
    elif media < mediana:
        print("Posible sesgo negativo o a la izquierda (sin una moda clara).")
    elif media == mediana:
        print("Posiblemente sin sesgo (sin una moda clara).")
    else:
        print("El sesgo no se puede determinar claramente sin una moda única.")


# Ejercicio 7
frase = input("Ingrese una frase o palabra: ")
ultima_letra = frase[-1].lower()  # Obtener la última letra y convertirla a minúscula

vocales = "aeiou"

if ultima_letra in vocales:
    frase_modificada = frase + "!"
    print(frase_modificada)
else:
    print(frase)


# Ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese la opción deseada (1, 2 o 3):\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula\n")

if opcion == '1':
    nombre_transformado = nombre.upper()
elif opcion == '2':
    nombre_transformado = nombre.lower()
elif opcion == '3':
    nombre_transformado = nombre.title()
else:
    nombre_transformado = "Opción inválida"

print("Resultado:", nombre_transformado)

# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif magnitud >= 3 and magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif magnitud >= 4 and magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud >= 5 and magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud >= 6 and magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:  # magnitud >= 7
    categoria = "Extremo (puede causar graves daños a gran escala)"

print("La magnitud del terremoto se clasifica como:", categoria)

# Ejercicio 10
def obtener_estacion(hemisferio, mes, dia):
    """Determina la estación del año según el hemisferio, mes y día."""
    mes = mes.lower()
    dia = int(dia)

    if hemisferio.upper() == 'N':
        if mes == 'diciembre' and dia >= 21 or mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia <= 20):
            return "invierno"
        elif (mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia <= 20):
            return "primavera"
        elif (mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia <= 20):
            return "verano"
        elif (mes == 'septiembre' and dia >= 21) or mes == 'octubre' or mes == 'noviembre' or (mes == 'diciembre' and dia <= 20):
            return "otoño"
        else:
            return "Fecha inválida"
    elif hemisferio.upper() == 'S':
        if mes == 'diciembre' and dia >= 21 or mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia <= 20):
            return "verano"
        elif (mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia <= 20):
            return "otoño"
        elif (mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia <= 20):
            return "invierno"
        elif (mes == 'septiembre' and dia >= 21) or mes == 'octubre' or mes == 'noviembre' or (mes == 'diciembre' and dia <= 20):
            return "primavera"
        else:
            return "Fecha inválida"
    else:
        return "Hemisferio inválido. Por favor, ingrese 'N' o 'S'."

# Solicitar información al usuario
hemisferio_usuario = input("¿En qué hemisferio se encuentra? (N/S): ")
mes_usuario = input("Ingrese el mes del año: ")
dia_usuario = input("Ingrese el día del mes: ")

# Obtener la estación
estacion_actual = obtener_estacion(hemisferio_usuario, mes_usuario, dia_usuario)

# Imprimir el resultado
print(f"En el hemisferio {hemisferio_usuario.upper()}, en {mes_usuario.capitalize()} el día {dia_usuario}, es {estacion_actual}.")
