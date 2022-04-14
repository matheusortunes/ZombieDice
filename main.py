"""
Estudante: Matheus Augusto Ortunes dos Santos
Curso: Análise e Desenvolvimento de Sistemas
Turma: 01
"""
import random
import time

x = 0
dado_verde = ("dado_verde", "CPCTPC")
dado_amarelo = ("dados_amarelo", "TPCTPC")
dado_vermelho = ("dados_vermelhos", "TPTCPT")


def pop_all(lista_2_, count=0):
    # Função simples para apagar o contéudo dentro de uma lista
    for n in lista_2_:
        lista_2_.pop(count)
        count = count + 1


def quantidade_jogadores(qtd_jogadores_, lista_de_jogadores_):  # Função responsável por definir a
    # quantidade de players que irão jogar
    qtd_jogadores_ = int(input("Digite a quantidade de jogadores: "))
    if qtd_jogadores_ < 2 or qtd_jogadores_ > 8:
        print("Quantidade de jogadores inválida, por favor, selecione entre 2 e 8 jogadores")
        return quantidade_jogadores(qtd_jogadores_, lista_de_jogadores_)  # Retorna a própria função, perguntando
        # novamente a quantidade de jogadores
    else:
        for i in range(qtd_jogadores_):
            jogador_ = input(f'Digite o nome do jogador {i + 1}: ')
            lista_de_jogadores_.append(jogador_)
        return qtd_jogadores_, lista_de_jogadores_


def compara_listas(dados_sorteados_, lista_2_, contador_):
    # Essa é uma lista extra para implementação da regra dos passos, todo dado que for jogado e que resultar em um passo
    # será adicionado a lista_2_, dessa forma consigo adicionar o mesmo dado que rolou P no próximo turno
    if lista_2_ is not []:
        for valor in lista_2_:
            contador_ = contador_ + 1
            dados_sorteados_.append(valor)
        return dados_sorteados_, lista_2_, contador_
    else:
        pass


def sorteia_tubo(contador_, dados_sorteados_, n=3):  # Essa função sorteia por padrão 3 dados entre os 13 do tubo
    if contador_ != 0:
        n = n - contador_
    for i in range(n):
        var = random.randint(0, len(tubo_de_dados) - 1)
        dados_sorteados_.append(tubo_de_dados[var])
        tubo_de_dados.pop(var)
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


def joga_dados(dados_sorteados_, cerebros_individual_, passos_individual_, tiros_individual_, lista_2_,
               indice_jogador_):  # Essa função joga os 3 dados
    # que foram sorteados no tubo
    for dado in dados_sorteados_:
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
            cerebros_individual_[indice_jogador_][1] += 1
        elif jogada == "P":
            passos_individual_[indice_jogador_][1] += 1
            lista_2_.append(dado)
        else:
            tiros_individual_[indice_jogador_][1] += 1

    return cerebros_individual_, passos_individual_, tiros_individual_, lista_2_


def score_individual(lista_de_jogadores_, cerebros_, passos_, tiros_, cerebros_individual_, passos_individual_,
                     tiros_individual_):
    # Essa função é responsável por criar a lista com as pontuações vazias para cada jogador da partida
    for jogador_ in lista_de_jogadores_:
        placar = [jogador_, 0]
        cerebros_.append(placar)
        passos_.append(placar)
        tiros_.append(placar)
        cerebros_individual_.append(placar)
        passos_individual_.append(placar)
        tiros_individual_.append(placar)

    return cerebros_, passos_, tiros_, cerebros_individual_, passos_individual_, tiros_individual_


def scoreboard(cerebros_, passos_, tiros_,
               indice_jogador_):  # Responsável apenas por imprimir o placar na tela do jogador
    print()
    print("===================================================")
    print("+++++               SCOREBOARD                +++++")
    print("===================================================")
    print()
    time.sleep(0.5)
    print(f'ATÉ AGORA VOCÊ COMEU {cerebros_[indice_jogador_][1]} CEREBRO(S)!')
    time.sleep(0.5)
    print(f'SUA CONTAGEM DE PASSOS É DE {passos_[indice_jogador_][1]} NO TOTAL!')
    time.sleep(0.5)
    print(f'VOCÊ TOMOU {tiros_[indice_jogador_][1]} TIRO(S)')
    print()


def continua_jogando():  # Pergunta se o jogador quer encerrar sua rodada ou continuar jogando os dados
    deseja_continuar = input("Deseja continuar jogando? (y/n): ")
    if deseja_continuar == "y":
        return 1
    elif deseja_continuar == "n":
        return 2
    else:
        print("Resposta inválida, por favor, responda utilizando y ou n")
        return continua_jogando()


while x == 0:  # Começando uma nova partida
    y = 0
    qtd_jogadores = 0
    lista_de_jogadores = []
    print("===================================================")
    print("+++        Seja bem vindo ao ZOMBIE DICE        +++")
    print("        +++  Começando um novo jogo  +++")
    print("===================================================")

    qtd_jogadores, lista_de_jogadores = quantidade_jogadores(qtd_jogadores, lista_de_jogadores)

    cerebros = []
    passos = []
    tiros = []
    cerebros_individual = []
    passos_individual = []
    tiros_individual = []
    cerebros, passos, tiros, cerebros_individual, passos_individual, tiros_individual = \
        score_individual(lista_de_jogadores, cerebros, passos, tiros, cerebros_individual,
                         passos_individual, tiros_individual)

    rodada = 1

    while y == 0:  # Começa uma nova rodada
        lista_2 = []
        contador = 0
        print()
        print("===================================================")
        print(f'     RODADA {rodada}, PREPARE-SE PARA COMER CÉREBROS!')
        print("===================================================")

        for jogador in lista_de_jogadores:  # Laço para todos os jogadores participarem do jogo
            indice_jogador = 1
            tubo_de_dados = [dado_verde[1], dado_verde[1], dado_verde[1], dado_verde[1], dado_verde[1],
                             dado_verde[1], dado_amarelo[1], dado_amarelo[1],
                             dado_amarelo[1], dado_amarelo[1], dado_vermelho[1], dado_vermelho[1], dado_vermelho[1]]
            continua = 1
            print()
            print(f'É a vez do jogador {jogador}')
            print()
            while continua == 1:  # Início do turno
                print(tubo_de_dados)

                dados_sorteados = []
                sorteio = []

                dados_sorteados, lista_2, contador = compara_listas(dados_sorteados, lista_2, contador)

                sorteia_tubo(contador, dados_sorteados)

                pop_all(lista_2)
                contador = 0

                time.sleep(1)
                print()
                print("===================================================")
                print("+++          É HORA DE JOGAR OS DADOS           +++")
                print("===================================================")
                print()

                cerebros_individual, passos_individual, tiros_individual, lista_2 = joga_dados(dados_sorteados,
                                                                                               cerebros_individual,
                                                                                               passos_individual,
                                                                                               tiros_individual,
                                                                                               lista_2, indice_jogador)
                
                if tiros_individual[indice_jogador][1] == 3:
                    print("VOCÊ TOMOU 3 TIROS! SUA PONTUAÇÃO DO TURNO SERÁ ZERADA!")
                    pop_all(cerebros_individual), pop_all(passos_individual), pop_all(tiros_individual)
                    continua = 2
                else:
                    cerebros[indice_jogador][1] = cerebros[indice_jogador][1] + cerebros_individual[indice_jogador][1]
                    passos[indice_jogador][1] = passos[indice_jogador][1] + passos_individual[indice_jogador][1]
                    tiros[indice_jogador][1] = tiros[indice_jogador][1] + tiros_individual[indice_jogador][1]
                    pop_all(cerebros_individual), pop_all(passos_individual), pop_all(tiros_individual)

                    print(f'PONTUACAO TOTAL: {cerebros}, {passos}, {tiros}')

                print(sorteio)

                time.sleep(1)
                scoreboard(cerebros, passos, tiros, indice_jogador)

                print(cerebros_individual, passos_individual, tiros_individual)

                print(cerebros, passos, tiros)

                # print(cerebros_total, passos_total, tiros_total)

                continua = continua_jogando()

            indice_jogador += 1

        rodada = rodada + 1

        # print("Acabou a rodada")
        # rodada = rodada + 1

        # if rodada == 3:
        #    y = 1

        # random.choices(lista_de_dados)
