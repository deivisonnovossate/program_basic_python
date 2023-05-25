#Funções

#Inicio da função dimensoesObjeto
def dimensoesobjeto():
    #Declarando as variáveis com valor de 0
    comprimento = 0
    largura = 0
    altura = 0

    # Inicio do loop
    while True:
        # Usando o Try e Except para tratar erros
        try:
            # Input para obter os valores da variáveis
            comprimento = int(input('Digite o comprimento do objeto (em cm): '))
            largura = int(input('Digite a largura do objeto (em cm): '))
            altura = int(input('Digite a altura do objeto (em cm): '))

        except ValueError:
            # Caso o usuário digite um valor não númerico
            print('Você digitou alguma dimensão do objeto com valor não númerico \n' +
                  'Por favor entre com as dimensões desejadas novamente!')
            continue
        else:
            # Calcula para sabermos qual o volume do objeto
            volume = comprimento * largura * altura
            print('O volume do objeto é (em cm³): {}'.format(volume))

            # Declarando a variável para receber o valor em R$
            rs = 0
            # Verificando na condicional os valores do quadro 1
            # Vamos retornar o rs para o calculo futuro do total a pagar
            if volume < 1000:
                rs += 10
                return rs
            elif 1000 >= volume < 10000:
                rs += 20
                return rs
            elif 10000 >= volume < 30000:
                rs += 30
                return rs
            elif 30000 >= volume < 100000:
                rs += 50
                return rs
            elif volume >= 100000:
                print(
                    'Não aceitamos objetos com dimensões tão grandes \n' + 'Entre com as dimensões desejadas novamente')
                continue
#Fim da função dimensoes Objeto
#Inicio da função pesoObjeto
def pesoobjeto():
    # Declarnado a variável Peso no valor de 0 para mais tarde receber o valor
    peso = 0
    # Iniciando o loop
    while True:
        # Usando o Try e Except para tratar erros
        try:
            # Input para obter os valores da variáveis
            peso = float(input('Digite quantos Kg tem o objeto (em Kg): '))
        except ValueError:
            # Caso o usuário digite um valor não númerico
            print('Você digitou alguma dimensão do objeto com valor não númerico \n' +
                  'Por favor digite o Kg do Objeto novamente!')
            continue
        else:
            # Declarando a variável para receber o multiplicador
            multi = 0
            # Verificando na condicional os valores do Quadro 2
            # Vamos retortar o valor do Multiplicador para calculo futuro no total a pagar
            if peso < 0.1:
                multi += 1
                return multi
            elif peso >= 0.1 or peso < 1:
                multi += 1.5
                return multi
            elif peso >= 1 or peso < 10:
                multi += 2
                return multi
            elif peso >= 10 or peso < 30:
                multi += 3
                return multi
            elif peso >= 30:
                print('Não aceitamos objetos tão pesados \n' +
                      'Entre com o peso desejado novamente')
#Fim da função peso Objeto
#Inicio da função rota Objeto
def rotaobjeto():
    # Iniciando o loop
    while True:
        # Exibindo o menu para o cliente escolher conforma as opções informadas
        print('Selecione a rota: \n' +
              'BR - De Brasília para Rio de Janeiro \n' +
              'BS - De Brasília para São Paulo \n' +
              'RB - De Rio de Janeiro para Brasília \n' +
              'RS - De Rio de Janeiro para São Paulo \n' +
              'SR - De São Paulo para Rio de Janeiro \n' +
              'SB - De São paulo para Brasília')
        # Recebendo a sigla digitada pelo cliente
        sigla = input('>> ')
        # convertendo para Maisculo caso o cliente digite em minusculo a sigla
        sigla = sigla.upper()
        # Usando o Try e Except para tratar erros
        try:
            # Condicional para verificar se o usuário digitou alguma sigla do menu
            if(sigla == 'BR') or (sigla == 'BS') or (sigla == 'RB') or \
                    (sigla == 'RS') or (sigla == 'SR') or (sigla == 'SB'):
                print('')
            else:
                # Caso não tenha digitado retornar a mensagem abaixo
                print('Você digitou uma rota que não existe \n' +
                      'Por favor entre com a rota desejada novamente')
        except ValueError:
            print('Você digitou uma rota que não existe \n' +
                  'Por favor entre com a rota desejada novamente')
            continue
        else:
            # Declarando a variável rotaMulti para receber o multiplicador
            rotaMulti = 0
            # Verificando na condicional os valores do Quadro 3
            # Vamos retortar o valor do Multiplicador da Rota para calculo futuro no total a pagar
            if sigla == 'BR':
                rotaMulti += 1.5
                return rotaMulti
            elif sigla == 'BS':
                rotaMulti += 1.2
                return rotaMulti
            elif sigla == 'RB':
                rotaMulti += 1.5
                return rotaMulti
            elif sigla == 'RS':
                rotaMulti += 1
                return rotaMulti
            elif sigla == 'SR':
                rotaMulti += 1
                return rotaMulti
            elif sigla == 'SB':
                rotaMulti += 1.2
                return rotaMulti
#Fim da função rota Objeto

#Inicio do Programa
print('Bem-vindo a Companhia de Logística Deivison Novossate')
# Inicializando as Funções e atribuindo a uma variável para fazer o calculo do total a pagar
dimensoes = dimensoesobjeto()
peso = pesoobjeto()
rota = rotaobjeto()

# calculo do total a pagar
total = dimensoes * peso * rota

#Mostrar para o Cliente
print('Total a pagar(R$): {} (dimensões: {} * peso: {} * rota: {})'.format(total, dimensoes, peso, rota))
