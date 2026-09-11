import src.Antonio_AHD3RA1.calculos as calculos
import src.Antonio_AHD3RA1.validaciones as validaciones

# Uso de funciones de 'calculos.py'
notas = [60, 90, 89]

promedio = calculos.calcular_promedio(notas)
print(promedio)

porcentaje = calculos.calcular_porcentaje(10, 90)
print(porcentaje)

estado = calculos.determinar_estado(80, 85)
print(estado)

nota_alta = calculos.obtener_nota_mayor(notas)
print(nota_alta)

nota_baja = calculos.obtener_nota_menor(notas)
print(nota_baja)

# Uso de las funciones de 'Validaciones.py'

rango = validaciones.esta_en_rango(30, 15, 45)
print(rango)

texto = validaciones.texto_no_vacio("Hola")
print(texto)

esPositivo = validaciones.es_positivo(10)
print(esPositivo)

notaValida = validaciones.nota_valida(-10)
print(notaValida)

asistencia = validaciones.asistencia_valida(12.5)
print(asistencia)