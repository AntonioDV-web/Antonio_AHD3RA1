# Recibe una Lista o tupla
def calcular_promedio(datos):
    promedio = sum(datos) / len(datos)
    return round(promedio, 2)

"""
    Calcula qué porcentaje representa una parte respecto al total.
    Si el total es 0, devuelve 0.0 para evitar una división por cero.
"""
def calcular_porcentaje(parte, total):
    if total == 0:
        return 0.0

    return round((parte / total) * 100, 2)

# Calcula promedio y asistencia para retornar el estado de Aprobado o Reprobado segun sea el caso
def determinar_estado(promedio, asistencia):
    if promedio >= 60 and asistencia >= 80:
        return "Aprobado"
    else:
        return "Reprobado"

def obtener_nota_mayor(datos):
    return max(datos)

def obtener_nota_menor(datos):
    return min(datos)

