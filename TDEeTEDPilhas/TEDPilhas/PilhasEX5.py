def imprimir_inversamente(pilha:list):
    inversa = []

    for i in pilha[::-1]:
        inversa.append(i)

    return inversa

x = imprimir_inversamente([4, 6, 7, 2, 9])
print(x)