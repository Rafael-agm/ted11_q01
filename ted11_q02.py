import numbers as np

# a. Criação da matriz A com valores inteiros randômicos
A = np.random.randint(1, 100, size=(10, 10))  # Valores entre 1 e 99
print("Matriz A:")
print(A)

# b. Soma de todos os valores da matriz A
soma_total = np.sum(A)
print("\nSoma de todos os valores da matriz A:", soma_total)

# c. Criação da matriz B, onde cada item é o valor da matriz A * 3
B = A * 3
print("\nMatriz B (A * 3):")
print(B)
