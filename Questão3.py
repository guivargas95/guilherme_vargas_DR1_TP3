'''
Questão 03
Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas, variando
de 0 até 10. Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.
Fluxo de exceção:
O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.
'''

def avaliar_candidato(quantidade_candidatos):
    vencedor = []
    for c in range(0,quantidade_candidatos):
        nome = str(input(f'Informe o nome do {c+1}º candidato: '))
        nota = float(input(f'Informe a nota do {c+1}º candidato: '))
        while nota > 10 or nota < 0:
            nota = float(input(f'Nota inválida. Informe valor entre 0 e 10.\nInforme a nota do {c+1}º candidato: '))
        if c == 0:
            vencedor.append(nome)
            vencedor.append(nota)
        else:
            if nota > vencedor[1]:
                vencedor[0] = nome
                vencedor[1] = nota
    print(f'O(a) vencedor(a) é {vencedor[0]} com nota {vencedor[1]} ')

quantidade_candidatos = int(input('Quantos candidatos deseja avaliar? '))
avaliar_candidato(quantidade_candidatos)