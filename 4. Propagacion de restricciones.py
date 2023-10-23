from constraint import Problem, AllDifferentConstraint, add_constraint

# Creación de un problema CSP
problem = Problem()

# Definición de variables y sus dominios
problem.addVariable("A", [1, 2, 3])
problem.addVariable("B", [4, 5, 6])
problem.addVariable("C", [7, 8, 9])

# Definición de restricciones
problem.addConstraint(lambda a, b, c: a + b == c, ("A", "B", "C"))
problem.addConstraint(AllDifferentConstraint(), ["A", "B", "C"])

# Crear una copia del problema con propagación de restricciones
problem_copy = problem.copy()
add_constraint(lambda a, b, c: a + b == c, ("A", "B", "C"), problem_copy)
add_constraint(AllDifferentConstraint(), ["A", "B", "C"], problem_copy)

# Obtener todas las soluciones
solutions = problem.getSolutions()
solutions_copy = problem_copy.getSolutions()

# Imprimir las soluciones
print("Soluciones sin propagación de restricciones:")
for solution in solutions:
    print(solution)

print("\nSoluciones con propagación de restricciones:")
for solution in solutions_copy:
    print(solution)
