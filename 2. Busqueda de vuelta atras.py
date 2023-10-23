def backtracking_csp(variables, dominios, restricciones):
    if not variables:
        return {}  # Todas las variables se han asignado, hemos encontrado una solución

    variable_actual = variables[0]
    for valor in dominios[variable_actual]:
        if es_valido(variable_actual, valor, restricciones):
            asignaciones = {variable_actual: valor}
            resultado = backtracking_csp(variables[1:], dominios, restricciones)
            if resultado is not None:
                asignaciones.update(resultado)
                return asignaciones

    return None

def es_valido(variable, valor, restricciones):
    for restriccion in restricciones:
        if variable in restriccion:
            otra_variable = restriccion[0] if restriccion[0] != variable else restriccion[1]
            if otra_variable in asignaciones and asignaciones[otra_variable] == valor:
                return False
    return True

# Ejemplo de uso
variables = ['A', 'B', 'C', 'D']
dominios = {
    'A': ['Rojo', 'Verde', 'Azul'],
    'B': ['Rojo', 'Verde'],
    'C': ['Verde', 'Azul'],
    'D': ['Rojo', 'Azul']
}

restricciones = [('A', 'B'), ('A', 'C'), ('A', 'D')]

asignaciones = {}
solucion = backtracking_csp(variables, dominios, restricciones)

if solucion:
    print("Solución encontrada:")
    for variable, valor in solucion.items():
        print(f"{variable}: {valor}")
else:
    print("No se encontró una solución válida.")
