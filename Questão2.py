'''
Questão 02
Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:
Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
Não tem direito a voto (menor de 16 anos).
Fluxo de exceção:
O programa deve verificar se a idade da pessoa é maior do que zero.
'''

def julgar_eleitor(idade):
    while idade <= 0:
        idade = int(input('Valor inválido. Informe a idade: '))
    if idade >= 18 and idade < 70:
        print(f'Com {idade} anos, o voto é obrigatório.')
    elif idade >= 16 or idade >= 70:
        print(f'Com {idade} anos, o voto é facultativo.')
    else:
        print(f'Com {idade} anos, não tem direito ao voto.')

idade = int(input('Informe a idade: '))
julgar_eleitor(idade)
