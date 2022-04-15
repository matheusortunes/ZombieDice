"""
Estudante: Matheus Augusto Ortunes dos Santos
Curso: Análise e Desenvolvimento de Sistemas
Turma: 01
"""
import random
import time
from sys import exit

dado_verde = ("dado_verde", "CPCTPC")
dado_amarelo = ("dados_amarelo", "TPCTPC")
dado_vermelho = ("dados_vermelhos", "TPTCPT")


def quantidade_jogadores(qtd_jogadores_, lista_de_jogadores_):  # Função responsável por definir a
    # quantidade de players que irão jogar
    qtd_jogadores_ = int(input("Digite a quantidade de jogadores: "))
    if qtd_jogadores_ < 2 or qtd_jogadores_ > 8:
        print("Quantidade de jogadores inválida, por favor, selecione entre 2 e 8 jogadores")
        return quantidade_jogadores(qtd_jogadores_, lista_de_jogadores_)  # Retorna a própria função, perguntando
        # novamente a quantidade de jogadores
    else:
        for i in range(qtd_jogadores_):  # Cada jogador é adicionando a lista de jogadores, além do nome do jogador
            # também é adicionando um par de chave-valor que representa o score dele em toda a partida
            nome_ = input(f'Digite o nome do jogador {i + 1}: ')
            jogador_ = {"Nome": nome_, "Score": 0}
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
            time.sleep(0.5)
            print(f'{jogador["Nome"]} sorteou o dado VERDE')
        elif dado == "TPCTPC":
            time.sleep(0.5)
            print(f'{jogador["Nome"]} sorteou o dado AMARELO')
        else:
            time.sleep(0.5)
            print(f'{jogador["Nome"]} sorteou o dado VERMELHO')


def joga_dados(dados_sorteados_, score_rodada_, lista_2_):  # Essa função joga os 3 dados que foram sorteados no tubo
    for dado in dados_sorteados_:  # Para cada dado sorteado, é feito uma jogada, caindo em uma das 6 faces do dado
        jogada = random.choice(dado)
        sorteio.append(jogada)
        if dado == "CPCTPC":  # Essa série de condicionais serve para verbalizar o jogo e o deixa mais interessante
            time.sleep(0.5)
            print(f'{jogador["Nome"]} jogou o dado VERDE e o resultado foi: {jogada}')
        elif dado == "TPCTPC":
            time.sleep(0.5)
            print(f'{jogador["Nome"]} jogou o dado AMARELO e o resultado foi: {jogada}')
        else:
            time.sleep(0.5)
            print(f'{jogador["Nome"]} jogou o dado VERMELHO e o resultado foi: {jogada}')

        if jogada == "C":  # Essa segunda série de condicionais é responsável por somar a face sorteada em score_rodada
            score_rodada_["CEREBROS"] += 1
        elif jogada == "P":
            score_rodada_["PASSOS"] += 1
            lista_2_.append(dado)
        else:
            score_rodada_["TIROS"] += 1

    return score_rodada_, lista_2_


def scoreboard(score_rodada_):  # Imprime o placar do turno na tela do jogador
    print()
    print("===================================================")
    print("+++++               SCOREBOARD                +++++")
    print("===================================================")
    print()
    time.sleep(0.5)
    print(f'ATÉ AGORA VOCÊ COMEU {score_rodada_["CEREBROS"]} CEREBRO(S) NESSE TURNO!')
    time.sleep(0.5)
    print(f'SUA CONTAGEM DE PASSOS É DE {score_rodada_["PASSOS"]} NO TURNO!')
    time.sleep(0.5)
    print(f'VOCÊ TOMOU {score_rodada_["TIROS"]} TIRO(S) NESSE TURNO')
    print()


def continua_jogando():  # Possibilita o jogador a encerrar seu turno ou continuar jogando
    parar = input("Deseja continuar jogando? (s/n): ")
    if parar == "s":
        return 1
    elif parar == "n":
        return 2
    else:
        print("Resposta inválida, por favor, responda utilizando y ou n")
        return continua_jogando()


fim = True
while fim:  # Começando uma nova partida
    y = 0
    qtd_jogadores = 0
    lista_de_jogadores = []
    print("===================================================")
    print("+++        Seja bem vindo ao ZOMBIE DICE        +++")
    print("        +++  Começando um novo jogo  +++")
    print("===================================================")
    qtd_jogadores, lista_de_jogadores = quantidade_jogadores(qtd_jogadores, lista_de_jogadores)
    indice_jogador = 0
    rodada = 1

    while y == 0:  # Começa uma nova rodada
        lista_2 = []
        contador = 0
        print()
        print("===================================================")
        print(f'     RODADA {rodada}, PREPARE-SE PARA COMER CÉREBROS!')
        print("===================================================")
        for jogador in lista_de_jogadores:  # Laço para todos os jogadores participarem do jogo
            tubo_de_dados = [dado_verde[1], dado_verde[1], dado_verde[1], dado_verde[1], dado_verde[1],
                             dado_verde[1], dado_amarelo[1], dado_amarelo[1],
                             dado_amarelo[1], dado_amarelo[1], dado_vermelho[1], dado_vermelho[1], dado_vermelho[1]]
            continua = 1
            print()
            print("===================================================")
            print(f'   +++      É A VEZ DO JOGADOR {jogador["Nome"]}    +++')
            print("===================================================")
            print()
            score_rodada = {"CEREBROS": 0, "PASSOS": 0, "TIROS": 0}
            while continua == 1:  # Início do turno
                dados_sorteados = []
                sorteio = []
                dados_sorteados, lista_2, contador = compara_listas(dados_sorteados, lista_2, contador)

                sorteia_tubo(contador, dados_sorteados)

                lista_2 = []
                contador = 0

                time.sleep(1)
                print()
                print("===================================================")
                print("+++          É HORA DE JOGAR OS DADOS           +++")
                print("===================================================")
                print()

                score_rodada, lista_2 = joga_dados(dados_sorteados, score_rodada, lista_2,)
                time.sleep(1)

                if score_rodada["TIROS"] < 3:
                    scoreboard(score_rodada)
                    turno = continua_jogando()
                    print()
                    if turno == 2:
                        jogador["Score"] += score_rodada["CEREBROS"]
                        if jogador["Score"] >= 13:
                            time.sleep(0.5)
                            print("===================================================")
                            print(f'+++   O JOGADOR {jogador["Nome"]} VENCEU A PARTIDA!    +++')
                            print("===================================================")
                            time.sleep(1)
                            exit()
                        else:
                            time.sleep(0.5)
                            print(f'SUA PONTUAÇÃO FOI SALVA! SEU SCORE NA PARTIDA É DE {jogador["Score"]} CÉREBROS')
                            time.sleep(0.5)
                            continua = 2
                else:
                    time.sleep(0.5)
                    print()
                    print("VOCÊ TOMOU 3 TIROS! SUA PONTUAÇÃO DO TURNO SERÁ ZERADA!")
                    print()
                    time.sleep(0.5)
                    print(f'SUA PONTUAÇÃO TOTAL É DE {jogador["Score"]} CÉREBROS')
                    continua = 2

            indice_jogador += 1

        rodada = rodada + 1

