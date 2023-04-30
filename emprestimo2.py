    

     #Desafio 01

    #Escreva um programa para aprovar um emprestimo bancarío
    # para a compra de uma casa.
    # o programa vai perguntar o valor da casa, o salario do comprador
    # e em quantos anos ele vai pagar.
    #calcule o valor da prestação mensal, sabendo que ela não pode exercer 30%
    # do salário ou então o empréstimo será negado.

casa = float(input('valor da casa: R$'))
salário = float(input('Salário do Comprador: R$'))
anos = int(input("Quantos anos de Financioamento?"))




mínimo = salário * 30 / 100



prestação = casa / (anos * 12)
print('para pagar uma casa de R${:.2f}  em {} anos ' .format(casa,anos), end="")
print(' a prestação será de R${:.2f}' .format(prestação))

if prestação <= mínimo:
    print("Empréstimo pode ser concedido!")

else:
    print("Empréstimo negado!")    

#print("Comprado tem que pagar {} e o mínimo de tanto -{}" .format(prestação))

