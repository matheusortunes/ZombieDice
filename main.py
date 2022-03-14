"""
Estudante: Matheus Augusto Ortunes dos Santos
Curso: Análise e Desenvolvimento de Sistemas
"""
import random

dado_verde = "CPCTPC"
dado_amarelo = "TPCTPC"
dado_vermelho = "TPTCPT"

teste = [('T', 1), ('P', 2)]


tubo_de_dados = [(dado_verde, 1), dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_amarelo, dado_amarelo,
                 dado_amarelo, dado_amarelo, dado_vermelho, dado_vermelho, dado_vermelho]


def quantidadeJogadores():
    qtd_jogadores = int(input("Digite a quantidade de jogadores: "))
    if qtd_jogadores < 2 or qtd_jogadores > 8:
        print("Quantidade de jogadores inválida, por favor, selecione entre 2 e 8 jogadores")
        return quantidadeJogadores()
    else:
        for i in range(qtd_jogadores):
            jogador = input(f'Digite o nome do jogador {i + 1}: ')
            lista_de_jogadores.append(jogador)


def sorteiaTubo(n=3): # Essa função sorteia por padrão 3 dados entre os 13 do tubo
    for i in range(n):
        dados_sorteados.append(random.choice(tubo_de_dados))
    print(dados_sorteados)


def jogaDados(): #Essa função joga os 3 dados que foram sorteados no tubo
    for dado in dados_sorteados:
        jogada = random.choice(dado)
        sorteio.append(jogada)


def continuaJogando():
    continua_jogando = input("Deseja continuar jogando? (y/n): ")
    if continua_jogando == "y":
        return 1
    elif continua_jogando == "n":
        return 2
    else:
        print("Resposta inválida, por favor, responda utilizando y ou n")
        return continuaJogando()

x = 0
y = 0

while x == 0:   #Começando uma nova partida
    lista_de_jogadores = []
    print("Seja bem vindo ao ZOMBIE DICE")
    print("Começando um novo jogo")
    print()

    quantidadeJogadores()

    rodada = 1

    while y == 0: #Começa uma nova rodada
        print()
        print(f'Começando a rodada {rodada}')

        for jogador in lista_de_jogadores:
            print(f'É a vez do jogador {jogador}')
            dados_sorteados = []
            sorteio = []

            sorteiaTubo()

            jogaDados()

            print(sorteio)

            varks = continuaJogando()
            print(varks)

            if varks == 1:
                print(sorteio)
                if "P" in sorteio:
                    passos = sorteio.count("P")
                    print(passos)

        print("Acabou a rodada")
        rodada = rodada + 1

        if rodada == 3:
            y = 1


        #random.choices(lista_de_dados)
