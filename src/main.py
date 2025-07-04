# main.py

from utils import input_inteiro, exibir_titulo, pausar

def menu_principal():
    while True:
        exibir_titulo("Sistema de Torneios de eSports")

        print("1. Gerenciar Jogadores")
        print("2. Gerenciar Times")
        print("3. Gerenciar Jogos")
        print("4. Gerenciar Partidas")
        print("0. Sair")

        opcao = input_inteiro("Escolha uma opção: ", minimo=0, maximo=4)

        if opcao == 1:
            menu_jogadores()
        elif opcao == 2:
            menu_times()
        elif opcao == 3:
            menu_jogos()
        elif opcao == 4:
            menu_partidas()
        elif opcao == 0:
            print("Saindo do sistema...")
            break


def menu_jogadores():
    exibir_titulo("Gerenciar Jogadores")
    print("1. Cadastrar jogador")
    print("2. Listar jogadores")
    print("3. Voltar ao menu principal")
    pausar()


def menu_times():
    exibir_titulo("Gerenciar Times")
    print("1. Criar time")
    print("2. Listar times")
    print("3. Voltar ao menu principal")
    pausar()


def menu_jogos():
    exibir_titulo("Gerenciar Jogos")
    print("1. Cadastrar jogo")
    print("2. Listar jogos")
    print("3. Voltar ao menu principal")
    pausar()


def menu_partidas():
    exibir_titulo("Gerenciar Partidas")
    print("1. Registrar partida")
    print("2. Listar partidas")
    print("3. Voltar ao menu principal")
    pausar()


if __name__ == "__main__":
    menu_principal()
