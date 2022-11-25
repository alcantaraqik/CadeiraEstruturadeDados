def TPilha2(A: list, B: list, vetor: list):
    for i in range(len(vetor)):
        if vetor[i] == 0:
            if len(A) > 0:
                A.pop()
            if len(B) > 0:
                B.pop()

        elif vetor[i] > 0:
            B.append(vetor[i])

        else:
            A.append(vetor[i])

    print(A, B)

t = TPilha2([],[],[-1,1,-2,2,0])