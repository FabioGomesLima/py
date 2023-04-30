    #Desafio 36 Empréstimo

    #Escreva um programa para aprovar um emprestimo bancarío
    # para a compra de uma casa.
    # o programa vai perguntar o valor da casa, o salario do comprador
    # e em quantos anos ele vai pagar.
    #calcule o valor da prestação mensal, sabendo que ela não pode exercer 30%
    # do salário ou então o empréstimo será negado.

casa = float(input   ('Valor da casa: R$'))
salário = float(input("salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento?"))

#a prestação não pode ultrapassar a porcentagem do salario
#dele então vou criar uma varialvel mínimo


mínimo = salário * 30 / 100

# calculando o valor da empréstação
prestação = casa /(anos * 12) #preço da casa dividido pela quantidade de meses que ele vai pagar
print('para pagar uma casa de R${:.2f} em {} anos' .format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação)) 
if prestação <= mínimo:
    print('Empréstimo pode ser concedido')
else: 

    print('Empréstimo negado!')   



#print('COMPARANDO tem que pagar {} e o mínimo é de tanto -{}'.format(prestação, mínimo))