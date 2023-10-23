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

# Imprimir las soluciones antes del acondicionamiento del corte
solutions = problem.getSolutions()
print("Soluciones antes del acondicionamiento del corte:")
for solution in solutions:
    print(solution)

# Realizar acondicionamiento del corte eliminando la variable "C"
problem.removeVariable("C")

# Imprimir las soluciones después del acondicionamiento del corte
solutions = problem.getSolutions()
print("\nSoluciones después del acondicionamiento del corte:")
for solution in solutions:
    print(solution)
