"""
Estudante: Matheus Augusto Ortunes dos Santos
Curso: Análise e Desenvolvimento de Sistemas
Turma: 01
"""
import random
import time

x = 0
y = 0
dado_verde = ("dado_verde","CPCTPC")
dado_amarelo = ("dados_amarelo","TPCTPC")
dado_vermelho = ("dados_vermelhos","TPTCPT")
tubo_de_dados = [dado_verde[1], dado_verde[1], dado_verde[1], dado_verde[1], dado_verde[1], dado_verde[1], dado_amarelo[1], dado_amarelo[1],
                 dado_amarelo[1], dado_amarelo[1], dado_vermelho[1], dado_vermelho[1], dado_vermelho[1]]


def quantidade_jogadores():  # Função responsável por definir a quantidade de players que irão jogar
    qtd_jogadores = int(input("Digite a quantidade de jogadores: "))
    if qtd_jogadores < 2 or qtd_jogadores > 8:
        print("Quantidade de jogadores inválida, por favor, selecione entre 2 e 8 jogadores")
        return quantidade_jogadores()   # Retorna a própria função, perguntando novamente a quantidade de jogadores
    else:
        for i in range(qtd_jogadores):
            jogador = input(f'Digite o nome do jogador {i + 1}: ')
            lista_de_jogadores.append(jogador)


def sorteia_tubo(n=3, contador):  # Essa função sorteia por padrão 3 dados entre os 13 do tubo
    if contador != 0:
        n = n - contador
    for i in range(n):
        var = random.randint(0, 12)
        dados_sorteados.append(tubo_de_dados[var])
        tubo_de_dados.pop(var)


def compara_listas(dados_sorteados, lista_2, contador):
    if lista_2 is not []:
        for valor in lista_2:
            contador = contador + 1
            dados_sorteados.append(valor)
        return dados_sorteados, lista_2, contador
    else:
        pass

# dados_sorteados é uma lista vazia declarada no inicio de cada rodada para cada um dos jogadores

    for dado in dados_sorteados:  # Esse laço apenas verbaliza mais o jogo, o deixando mais interessante para o jogador
        if dado == "CPCTPC":
            time.sleep(1)
            print(f'{jogador} sorteou o dado VERDE')
        elif dado == "TPCTPC":
            time.sleep(1)
            print(f'{jogador} sorteou o dado AMARELO')
        else:
            time.sleep(1)
            print(f'{jogador} sorteou o dado VERMELHO')


def joga_dados(dados_sorteados, cerebros, passos, tiros, flag, lista_2):  # Essa função joga os 3 dados
    # que foram sorteados no tubo
    for dado in dados_sorteados:
        jogada = random.choice(dado)
        sorteio.append(jogada)
        if dado == "CPCTPC":
            time.sleep(1)
            print(f'{jogador} jogou o dado VERDE e o resultado foi: {jogada}')
        elif dado == "TPCTPC":
            time.sleep(1)
            print(f'{jogador} jogou o dado AMARELO e o resultado foi: {jogada}')
        else:
            time.sleep(1)
            print(f'{jogador} jogou o dado VERMELHO e o resultado foi: {jogada}')

        if jogada == "C":
            cerebros = cerebros + 1
        elif jogada == "P":
            passos = passos + 1
            flag = True
            lista_2.append(dado)
        else:
            tiros = tiros + 1

    return cerebros, passos, tiros, flag, lista_2


def scoreboard(cerebros, passos, tiros):  # Responsável apenas por imprimir o placar na tela do jogador
    print()
    print("===================================================")
    print("+++++               SCOREBOARD                +++++")
    print("===================================================")
    print()
    time.sleep(0.5)
    print(f'ATÉ AGORA VOCÊ COMEU {cerebros} CEREBRO(S)!')
    time.sleep(0.5)
    print(f'SUA CONTAGEM DE PASSOS É DE {passos} NO TOTAL!')
    time.sleep(0.5)
    print(f'VOCÊ TOMOU {tiros} TIRO(S)')
    print()


def continua_jogando(): # Pergunta se o jogador quer encerrar sua rodada ou continuar jogando os dados
    deseja_continuar = input("Deseja continuar jogando? (y/n): ")
    if deseja_continuar == "y":
        return 1
    elif deseja_continuar == "n":
        return 2
    else:
        print("Resposta inválida, por favor, responda utilizando y ou n")
        return continua_jogando()


while x == 0:   # Começando uma nova partida
    lista_de_jogadores = []
    tiros = 0
    passos = 0
    cerebros = 0
    print("===================================================")
    print("+++        Seja bem vindo ao ZOMBIE DICE        +++")
    print("        +++  Começando um novo jogo  +++")
    print("===================================================")

    quantidade_jogadores()

    rodada = 1

    while y == 0:  # Começa uma nova rodada
        lista_2 = []
        flag = False
        contador = 0
        print()
        print(f'RODADA {rodada}, PREPARE-SE PARA COMER CÉREBROS!')

        for jogador in lista_de_jogadores: # Laço para todos os jogadores participarem do jogo
            continua = 1
            print(f'É a vez do jogador {jogador}')
            print()
            while continua == 1:
                dados_sorteados = []
                sorteio = []

                dados_sorteados, lista_2 = compara_listas(dados_sorteados, lista_2)

                sorteia_tubo()

                time.sleep(1)
                print()
                print("===================================================")
                print("+++          É HORA DE JOGAR OS DADOS           +++")
                print("===================================================")
                print()

                dados_sorteados, passos, tiros, flag, lista_2 = joga_dados(dados_sorteados, cerebros, passos, tiros,
                                                                           flag, lista_2)

                print(f'LISTA 2 --> {lista_2}')

                print(sorteio)

                time.sleep(1)
                scoreboard(cerebros, passos, tiros)

                continua = continua_jogando()





        #print("Acabou a rodada")
        #rodada = rodada + 1

        #if rodada == 3:
        #    y = 1


        #random.choices(lista_de_dados)
