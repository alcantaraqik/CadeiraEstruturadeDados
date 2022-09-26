'''Questões'''

'''1 - Faça um programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por 
aluno e apresentar:

a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;

b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;

c) A mensagem "Aprovado com Distinção", se a média for igual a 10.

2- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue 
pedindo até que o usuário informe um valor válido.


3- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
C = 5 * ((F-32) / 9).

4- Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não 
bissexto.

5 - Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo 
usuário.

6 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.

7- Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado.

Obs: Deve ser enviado apenas o link do github com acesso aos códigos.'''
'''RESPOSTAS'''



'''1'''
'''nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
if media == 10:
    print('Aprovado com Distinção')
elif media < 7:
    print('Reprovado')
else:
    print('Aprovado')'''

'''2'''

'''n1 = float(input('Digite um valor de 0 a 10: '))
while n1 >10:
    print('invalida')
    n1 = float(input('Digite um valor de 0 a 10: '))'''



'''3'''

'''fr = float(input('Quantos graus em Fahrenheit? '))
c = round(5 * ((fr-32) / 9), 1)
print(f'{fr} graus Fahrenheit é o mesmo que {c} graus Celsius ')'''

'''4'''

'''print('Calculador de ano bissexto')
print('-------------')
bissexto=int(input('Digite o ano que deseja descobrir se é bissexto: '))
resp = bissexto % 4
if resp == 0:
    print('Este ano é bissexto!!!')
else:
    print('Este ano nao é bissexto')'''

'''5'''

'''numero = int(input('digite um numero: '))
lista = []

for i in range (numero+1):
    if i % 2 == 1 and i !=2:
        lista.append(i)

print(lista)'''


'''6'''
'''pessoas = []

pessoa1 = [input('Digite sua idade e altura: ')]
pessoas.append(pessoa1)

pessoa2 = [input('Digite sua idade e altura: ')]
pessoas.append(pessoa2)

pessoa3 = [input('Digite sua idade e altura: ')]
pessoas.append(pessoa3)

pessoa4 = [input('Digite sua idade e altura: ')]
pessoas.append(pessoa4)

pessoa5 = [input('Digite sua idade e altura: ')]
pessoas.append(pessoa5)

pessoas.reverse()
print(pessoas)'''

'''7'''
'''numero = int(input('Digite um numero que queira fazer a reversao: '))
numero_inverso = numero * -1

print(numero_inverso)'''


