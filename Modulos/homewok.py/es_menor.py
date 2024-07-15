"""Modulo de menor de edad"""
def f_es_menor(lista:list):   # Las anotaciones son importantes,
    """función para saber el número menor de una lista"""
    menor=lista[0]
    for n in lista:
        if n < menor:
            menor=n
    return menor