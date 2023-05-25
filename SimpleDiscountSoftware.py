print('Software created by Deivison Novossate')
#Variável receberá o valor unitário do produto
valor_produto = float(input('Digite o valor do produto: '))
#Variável receberá a quantidade do produto
qtd_produto = int(input('Digite a quantidade do produto: '))

# Realizando verificação para os descontos
if (qtd_produto <= 9):
    desconto = 0
elif (qtd_produto >= 10 and qtd_produto <= 99):
    desconto = 0.05
elif (qtd_produto >= 100 and qtd_produto <= 999):
    desconto = 0.10
else:
    desconto = 0.15

# Calculado o valor total Produto x Quantidade
valor_total = valor_produto * qtd_produto
# Calculando o desconto
valor_com_desconto = valor_total - (valor_total * desconto)
#Exibindo na tela os valores sem desconto e com desconto
print('O valor do produto SEM desconto é: R$ {}'.format(valor_total))
print('O valor do produto COM desconto é: R$ {:.2f}'.format(valor_com_desconto))
