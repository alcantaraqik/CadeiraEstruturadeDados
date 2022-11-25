def TPilha(vetor):
    pilhas = []

    if len(vetor) == 15:
        for i in range(len(vetor)):
            if vetor[i] % 2 == 0:
                pilhas.append(vetor[i])
            else:
                if len(pilhas) > 0:
                    pilhas.pop()

        for i in range(len(pilhas)):
            print(pilhas[i])

        pilhas.clear()


x = TPilha([1, 2, 3, 4, 5, 6, 7, 9, 9, 16, 21, 82, 12, 74, 42])