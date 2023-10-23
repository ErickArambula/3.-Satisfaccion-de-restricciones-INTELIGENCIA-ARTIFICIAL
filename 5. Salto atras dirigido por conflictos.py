def conflicto(estado, fila, columna):
    for i in range(fila):
        if estado[i] == columna or \
           estado[i] - i == columna - fila or \
           estado[i] + i == columna + fila:
            return True
    return False

def salto_atras_dirigido_conflictos(n, max_iter):
    estado_actual = [0] * n  # Inicializa un tablero vacío

    for _ in range(max_iter):
        conflicto_encontrado = False
        for fila in range(n):
            for columna in range(n):
                if not conflicto(estado_actual, fila, columna):
                    estado_actual[fila] = columna
                    break
            else:
                conflicto_encontrado = True
                break

        if not conflicto_encontrado:
            return estado_actual

    return None

# Ejemplo de uso
n = 8
max_iter = 1000
solucion = salto_atras_dirigido_conflictos(n, max_iter)

if solucion:
    print("Solución encontrada:")
    for fila, columna in enumerate(solucion):
        print(f"Fila {fila + 1}: Columna {columna + 1}")
else:
    print("No se encontró una solución válida en el número máximo de iteraciones.")
