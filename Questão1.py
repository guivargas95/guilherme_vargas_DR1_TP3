'''
Questão 01
Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais, considerando
o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.
Ao usuário do programa serão solicitados o valor total do consumo, em reais, o número total de pessoas e o percentual
do serviço prestado, entre 0 e 100.

Fluxo de exceção:
O programa deve verificar se o número total de pessoas é maior do que zero.
O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100.
Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.
Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), usando vírgula como
separador de casa decimal, em vez de pontos.
'''

def pagar_conta(valor_total,quant_pessoas,taxa):
    while True:
        if valor_total <= 0:
            valor_total = float(input('Valor inválido. Informe o valor total: R$ '))
        elif quant_pessoas <= 0:
            quant_pessoas = int(input('Valor inválido. Informe a quantidade de pessoas: '))
        elif taxa > 100 or taxa < 0:
            taxa = int(input('Valor inválido. Informe o valor da taxa: '))
        else:
            break
    valor_total = float((valor_total * (taxa/100)) + valor_total)
    valor_dividido = float(valor_total / quant_pessoas)
    valor_total = str((f'{valor_total:.2f}')).replace('.',',')
    valor_dividido = str((f'{valor_dividido:.2f}')).replace('.',',')
    print(f'\nO valor total da conta com a taxa é de R${valor_total}.\nDividindo a conta por {quant_pessoas} pessoa(s)'
          f', cada um deverá pagar R${valor_dividido}.')

valor_total = float(input('Informe o valor total da conta: R$ '))
quant_pessoas = int(input('Informe a quantidade de pessoas: '))
taxa = float(input('Informe o valor da taxa, entre 0 e 100: '))
pagar_conta(valor_total,quant_pessoas,taxa)