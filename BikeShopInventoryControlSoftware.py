# ---------- INICIO Variáveis Globais ---------- #
# Declando a lista e uma variável para o codigo da peça
lista_pecas = []
codigo_peca = 0


# ---------- FIM Variáveis Globais ---------- #

# ---------- INICIO Cadastrar Peça ---------- #
def cadastrarPeca(codigo):  # Iniciando a Função Cadastrar Peça
    print('Você Selecionou a Opção de Cadastrar Peça')  # Exibindo qual opção do menu foi selecionada

    nome = input('Por favor entre com o NOME da peça: ')  # Pegandno o nome pelo input
    fabricante = input('Por favor entre com o FABRICANTE da peça: ')  # Pegandno o nome do fabricante pelo input
    preco = int(input('Por favor entre com o VALOR(R$) da peça: '))  # Pegandno o preco pelo input

    # Dicionario de peças
    dicionario_peca = {'codigo': codigo,
                       'nome': nome,
                       'fabricante': fabricante,
                       'preco': preco}
    lista_pecas.append(dicionario_peca.copy())  # Adicionando no dicionário


# ---------- FIM Cadastrar Peça ---------- #

# ---------- INICIO Consultar Peça ---------- #
def consultar_peca():  # Iniciando a função Consultar Peça
    while True:

        print('\nVocê Selecionou a Opção Consultar Peças')  # Exibindo qual opção do menu foi selecionada
        menu_consultar = input(' \nEscolha a opção desejada: \n' +
                               '1 - Consultar Todas as Peças \n' +
                               '2 - Consultar Peças por Código \n' +
                               '3 - Consultar Peças por Fabricante \n' +
                               '4 - Retornar \n' +
                               '>> ')
        # Realiazando a condição para opção escolhida pelo usuário
        if menu_consultar == '1':
            print('Você escolheu a opção Consultar todas as peças')
            for peca in lista_pecas:  # variavel peca vai varrer toda lista de lista de peças
                print('---------------------------')
                for key, value in peca.items():  # Varrer todos as pecas chave e valor do dicionario peças
                    print('{} : {}'.format(key, value))

        elif menu_consultar == '2':
            print('Você escolheu a opção Consultar Peças por Código')
            valor_desejado = int(input('Entre com o código desejado: '))
            for peca in lista_pecas:
                if peca[
                    'codigo'] == valor_desejado:  # o valor do campo código desse dicionário é igual o valor desejado?
                    print('---------------------------')
                    for key, value in peca.items():  # Varrer todos as pecas chave e valor do dicionario peças
                        print('{} : {}'.format(key, value))


        elif menu_consultar == '3':
            print('Você escolheu a opção Consultar Peças por Fabricante')
            valor_desejado = input('Entre com o fabricante desejado: ')
            for peca in lista_pecas:
                if peca[
                    'fabricante'] == valor_desejado:  # o valor do campo fabricante desse dicionário é igual o valor desejado?
                    print('---------------------------')
                    for key, value in peca.items():  # Varrer todos as pecas chave e valor do dicionario peças
                        print('{} : {}'.format(key, value))

        elif menu_consultar == '4':
            return  # sai da função consultar Peça e volta para Main
        else:
            print('Opção Inválida. Tente Novamente')
            continue


# ---------- FIM Consultar Peça ---------- #

# ---------- INICIO Remover Peça ---------- #
def remover_peca():  # Iniciando a função remover Peça
    print('Você Selecionou a Opção de Remover Peça')  # Exibindo qual opção do menu foi selecionada
    valor_desejado = int(input('Entre com o código da peça a ser removida: '))
    for peca in lista_pecas:
        if peca['codigo'] == valor_desejado:
            lista_pecas.remove(peca)
            print('A peça foi removida!')


# ---------- FIM Remover Peça ---------- #

# ---------- INICIO de Main ---------- #
print('\nBem-vindo ao Controle de Estoque da Bicicletaria do Deivison Novossate')
while True:
    menu_principal = input('Escolha a opção desejada: \n' +
                           '1 - Cadastrar Peças \n' +
                           '2 - Consultar Peças \n' +
                           '3 - Remover Peças \n' +
                           '4 - Sair \n' +
                           '>> ')
    if menu_principal == '1':
        codigo_peca += 1
        cadastrarPeca(codigo_peca)
    elif menu_principal == '2':
        consultar_peca()
    elif menu_principal == '3':
        remover_peca()
    elif menu_principal == '4':
        break
    else:
        print('Opção Inválida. Por favor escolhar opções do menu!')
        continue
# ---------- FIM de Main ---------- #
