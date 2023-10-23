from constraint import Problem, AllDifferentConstraint

# Creación de un problema CSP
problem = Problem()

# Definición de variables y sus dominios
problem.addVariable("A", [1, 2, 3])
problem.addVariable("B", [4, 5, 6])
problem.addVariable("C", [7, 8, 9])

# Definición de restricciones
problem.addConstraint(lambda a, b, c: a + b == c, ("A", "B", "C"))
problem.addConstraint(AllDifferentConstraint(), ["A", "B", "C"])

# Obtener todas las soluciones
solutions = problem.getSolutions()

# Imprimir las soluciones
for solution in solutions:
    print("Solución:")
    for var in solution:
        print(f"{var}: {solution[var]}")
    print("-" * 10)



