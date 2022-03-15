"""
Estudante: Matheus Augusto Ortunes dos Santos
Curso: Análise e Desenvolvimento de Sistemas
"""
import random
import time


x = 0
y = 0
dado_verde = "CPCTPC"
dado_amarelo = "TPCTPC"
dado_vermelho = "TPTCPT"
tubo_de_dados = [dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_amarelo, dado_amarelo,
                 dado_amarelo, dado_amarelo, dado_vermelho, dado_vermelho, dado_vermelho]


def quantidade_jogadores(): #Função responsável por definir a quantidade de players que irão jogar
    qtd_jogadores = int(input("Digite a quantidade de jogadores: "))
    if qtd_jogadores < 2 or qtd_jogadores > 8:
        print("Quantidade de jogadores inválida, por favor, selecione entre 2 e 8 jogadores")
        return quantidade_jogadores()   #Retorna a própria função, perguntando novamente a quantidade de jogadores
    else:
        for i in range(qtd_jogadores):
            jogador = input(f'Digite o nome do jogador {i + 1}: ')
            lista_de_jogadores.append(jogador)


def sorteia_tubo(n=3): # Essa função sorteia por padrão 3 dados entre os 13 do tubo
    for i in range(n):
        dados_sorteados.append(random.choice(tubo_de_dados))
#dados_sorteados é uma lista vazia declarada no inicio de cada rodada para cada um dos jogadores

    for dado in dados_sorteados:  #Esse laço apenas verbaliza mais o jogo, o deixando mais interessante para o jogador
        if dado == "CPCTPC":
            time.sleep(1)
            print(f'{jogador} sorteou o dado VERDE')
        elif dado == "TPCTPC":
            time.sleep(1)
            print(f'{jogador} sorteou o dado AMARELO')
        else:
            time.sleep(1)
            print(f'{jogador} sorteou o dado VERMELHO')


def joga_dados(): #Essa função joga os 3 dados que foram sorteados no tubo
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


def continua_jogando(): #Pergunta se o jogador quer encerrar sua rodada ou continuar jogando os dados
    deseja_continuar = input("Deseja continuar jogando? (y/n): ")
    if deseja_continuar == "y":
        return 1
    elif deseja_continuar == "n":
        return 2
    else:
        print("Resposta inválida, por favor, responda utilizando y ou n")
        return continua_jogando()


while x == 0:   #Começando uma nova partida
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

    while y == 0: #Começa uma nova rodada
        print()
        print(f'RODADA {rodada}, PREPARE-SE PARA COMER CÉREBROS!')

        for jogador in lista_de_jogadores: #Laço para todos os jogadores participarem do jogo
            print(f'É a vez do jogador {jogador}')
            print()
            dados_sorteados = []
            sorteio = []

            sorteia_tubo()

            time.sleep(1)
            print()
            print("===================================================")
            print("+++          É HORA DE JOGAR OS DADOS           +++")
            print("===================================================")
            print()

            joga_dados()

            print(sorteio)

            varks = continua_jogando()

            if varks == 1:
                print(sorteio)
                #if "P" in sorteio:
                 #   passos = sorteio.count("P")
                 #   print(passos)

        print("Acabou a rodada")
        rodada = rodada + 1

        if rodada == 3:
            y = 1


        #random.choices(lista_de_dados)
