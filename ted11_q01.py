# Inicializa o vetor
VET = []

# Lê 10 números
for i in range(10):
    num = int(input(f"Digite o número {i + 1}: "))
    VET.append(num)

# Verifica números repetidos
for i in range(10):
    repetidos = False
    posicoes = []

    for j in range(10):
        if i != j and VET[i] == VET[j]:
            repetidos = True
            posicoes.append(j)

    if repetidos:
        print(f"O número {VET[i]} está repetido nas posições: {i}", end=' ')
        print(*posicoes)  # Imprime as posições em que o número está repetido

