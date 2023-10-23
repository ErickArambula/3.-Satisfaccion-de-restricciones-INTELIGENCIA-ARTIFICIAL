import random

def conflicto(estado, fila, columna):
    for i in range(fila):
        if estado[i] == columna or \
           estado[i] - i == columna - fila or \
           estado[i] + i == columna + fila:
            return True
    return False

def calcular_conflictos(estado):
    n = len(estado)
    conflictos = 0
    for fila in range(n):
        for otra_fila in range(fila + 1, n):
            if conflicto(estado, fila, estado[otra_fila]):
                conflictos += 1
    return conflictos

def min_conflictos(n, max_iter):
    estado_actual = [random.randint(0, n-1) for _ in range(n)]

    for _ in range(max_iter):
        conflictos = calcular_conflictos(estado_actual)
        if conflictos == 0:
            return estado_actual
        fila = random.randint(0, n - 1)
        columna_original = estado_actual[fila]
        mejores_columnas = [columna_original]
        for columna in range(n):
            if columna != columna_original:
                estado_actual[fila] = columna
                nuevos_conflictos = calcular_conflictos(estado_actual)
                if nuevos_conflictos < conflictos:
                    mejores_columnas = [columna]
                elif nuevos_conflictos == conflictos:
                    mejores_columnas.append(columna)
        estado_actual[fila] = random.choice(mejores_columnas)

    return None

# Ejemplo de uso
n = 8
max_iter = 1000
solucion = min_conflictos(n, max_iter)

if solucion:
    print("Solución encontrada:")
    for fila, columna in enumerate(solucion):
        print(f"Fila {fila + 1}: Columna {columna + 1}")
else:
    print("No se encontró una solución válida en el número máximo de iteraciones.")
