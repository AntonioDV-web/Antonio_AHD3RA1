import src.Antonio_AHD3RA1.calculos as calculos
import src.Antonio_AHD3RA1.validaciones as validaciones

# Uso de funciones de 'calculos.py'
notas = []
print("----- Ingrese 3 notas para realizar calculos -----")

for i in range(3):
    while True:
        entrada_texto = input(f"Ingrese la nota No. {i + 1}: ")
        if entrada_texto.replace('.', '', 1).isdigit():
            entrada = float(entrada_texto)
            notas.append(entrada)
            break
        else:
            print("Error: Ingrese un número válido.")

print("\nNotas ingresadas con éxito:", notas)
print(f"El promedio de las notas ingresadas es: {calculos.calcular_promedio(notas)}")
print(f"El estado seún las notas es: {calculos.determinar_estado(calculos.calcular_promedio(notas), 80)}")
print(f"La nota más alta es: {calculos.obtener_nota_mayor(notas)}")
print(f"La nota más baja es: {calculos.obtener_nota_menor(notas)}")

print("-"* 50)

print(f"----- Calcular porcentaje -----")
parte = float(input("Ingrese el valor de la parte: "))
total = float(input("Ingrese el valor del total: "))
print(f"El {parte}% de {total} es: {calculos.calcular_porcentaje(parte, total)}")
print("-"* 50)


# Uso de las funciones de 'Validaciones.py'

print("----- Validaciones -----")
print("comprobar si el valor ingresado se encuentra entre el mínimo y máximo permitidos")
valor_max = int(input("Ingrese el valor máximo: "))
valor_min = int(input("Ingrese el valor mínimo: "))
valor = int(input("Ingrese el valor a comprobar: "))

print(f"El valor ingresado se encuentra entre el valor máximo o mínimo?: {validaciones.esta_en_rango(valor, valor_min, valor_max)}")
print("-" * 50)

print(f"Verificador de texto no vacío o solo espacios.")
texto = input("Ingrese el texto que desea verificar: ")
print(f"El texto no esta vacío o solo tiene espacios?: {validaciones.texto_no_vacio(texto)}")
print("-" * 50)

print("Comprobar si el número es mayor a cero.")
numero = int(input("Ingrese el número: "))
print(f"El número ingresado es mayor a cero?: {validaciones.es_positivo(numero)}")
print("-" * 50)

print("Validar si la nota esta entre 0 y 100.")
nota = int(input("Ingrese la nota: "))
print(f"La nota ingresada es valida?: {validaciones.nota_valida(nota)}")
print("-" * 50)

print("Verificar que un porcentaje de asistencia se encuentre entre 0 y 100.")
porcentaje = float(input("Ingrese el porcentaje: "))
print(f"El porcentaje ingresado es valido?: {validaciones.asistencia_valida(porcentaje)}")





