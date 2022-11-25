def pilhas_iguais(pilha1: list, pilha2: list):
    if pilha1 == pilha2:
        return True
    else:
        return False

a = pilhas_iguais([1, 2, 3, 4, 5],[1, 2, 3, 4, 5])
b = pilhas_iguais([1, 2, 3, 4, 5],[5, 4, 3, 2, 1])
print(a)
print(b)