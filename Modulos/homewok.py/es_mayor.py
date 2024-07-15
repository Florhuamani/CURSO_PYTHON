"""modulo de es menor"""
def f_es_mayor(lista:list):
    """función para saber el número mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n > mayor:
            mayor=n
    return mayor