"""
Recibir un valor y comprobar si se encuentra entre el mínimo y máximo
permitidos. Debe devolver True o False.
"""
def esta_en_rango(valor, minimo, maximo):
    if valor < minimo or valor > maximo:
        return False
    else:
        return True

"""
Comprobar que una cadena de texto no esté vacía ni contenga
únicamente espacios. Debe devolver True o False.
"""
def texto_no_vacio(texto):
    tx = texto.replace(' ','')
    if len(tx) == 0:
        return False
    else:
        return True
# Comprobar si un número es mayor que cero y devolver True o False.
def es_positivo(valor):
    return 0 <= valor

# Verificar que una nota se encuentre entre 0 y 100. Debe devolver True o False.
def nota_valida(nota):
    return 0 <= nota <= 100
"""
Verificar que un porcentaje de asistencia se encuentre entre 0 y 100.
Debe devolver True o False.
"""
def asistencia_valida(valor: float) -> bool:
    return 0 <= valor <= 100