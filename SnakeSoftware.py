print('Bem-vindo a Lanchonete do Deivison Novossate')
print('----------------------CARDÁPIO----------------------')
print('| CÓDIGO |   DESCRIÇÃO              |    VALOR     |')
print('|  100   |   Cachorro Quente        |    R$  9,00  |')
print('|  101   |   Cachorro Quente Duplo  |    R$ 11,00  |')
print('|  102   |   X-Egg                  |    R$ 12,00  |')
print('|  103   |   X-Salada               |    R$ 12,00  |')
print('|  104   |   X-Bacon                |    R$ 14,00  |')
print('|  105   |   X-Tudo                 |    R$ 17,00  |')
print('|  200   |   Refrigerante Lata      |    R$  5,00  |')
print('|  201   |   Chá Gelado             |    R$  4,00  |')
print('----------------------------------------------------')

# Variável para receber o valor do pedido e logo depois ir somando caso usuário peça mais algum lanche ou bebida
valor_a_pagar = 0

# Iniciando o Laço de repetição
while True:
    # Variável para receber o código desejado do cliente
    codigo = input('Entre com o código desejado: ')
    # Condição para verificar se o usuário está digitando codigo inválido
    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201':
        print('Opção Inválida!')
        continue
    # Iniciando as verificações com os códigos corretos imprimindo o que usuário escolheu e adicionado o valor na variável valor_a_pagar
    if codigo == '100':
        print('Você pediu um Cachorro-Quente no valor de R$ 9,00')
        valor_a_pagar += 9 # Varíável recebendo o valor dela mesmo mais o do lanche
    elif codigo == '101':
        print('Você pediu um Cachorro Quente-Duplo no valor de R$ 11,00')
        valor_a_pagar += 11  # Varíável recebendo o valor dela mesmo mais o do lanche
    elif codigo == '102':
        print('Você pediu um X-Egg  no valor de R$ 12,00')
        valor_a_pagar += 12  # Varíável recebendo o valor dela mesmo mais o do lanche
    elif codigo == '103':
        print('Você pediu um X-Salada no valor de R$ 12,00')
        valor_a_pagar += 12  # Varíável recebendo o valor dela mesmo mais o do lanche
    elif codigo == '104':
        print('Você pediu um X-Bacon  no valor de R$ 14,00')
        valor_a_pagar += 14  # Varíável recebendo o valor dela mesmo mais o do lanche
    elif codigo == '105':
        print('Você pediu um X-Tudo no valor de R$ 17,00')
        valor_a_pagar += 17  # Varíável recebendo o valor dela mesmo mais o do lanche
    elif codigo == '200':
        print('Você pediu um Refrigerante Lata no valor de R$ 5,00')
        valor_a_pagar += 5  # Varíável recebendo o valor dela mesmo mais o do lanche
    else:
        print('Você pediu um Chá Gelado  no valor de R$ 4,00')
        valor_a_pagar += 4  # Varíável recebendo o valor dela mesmo mais o do lanche

    # Informando se o usuário vai querer mais alguma coisa
    print('Deseja pedir mais alguma coisa? ')
    print('1 - SIM')
    print('0 - NÃO')
    pedir_mais = input('')

    # verificação do usuário se vai querer mais alguma coisa
    # se sim vamos voltar ao menu
    if pedir_mais == '1':
        continue
    # Se não vamos encerrar o programa inrformando o valor que deve ser pago
    else:
        print('O tatal a ser pago é: R$ {:.2f}'.format(valor_a_pagar))
        break
