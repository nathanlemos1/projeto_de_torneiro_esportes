# src/main.py

import sys
from db_manager import (
    cadastrar_jogador,
    listar_jogadores,
    cadastrar_time,
    listar_times,
    cadastrar_jogo,
    listar_jogos,
    registrar_partida,
    listar_partidas
)
from utils import limpar_tela, pausar

def menu():
    while True:
        limpar_tela()
        print("=== Sistema de Torneios de eSports ===\n")
        print("1. Cadastrar jogador")
        print("2. Listar jogadores")
        print("3. Criar time")
        print("4. Listar times")
        print("5. Cadastrar jogo")
        print("6. Listar jogos")
        print("7. Registrar partida")
        print("8. Listar partidas")
        print("0. Sair\n")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_jogador()
        elif escolha == "2":
            listar_jogadores()
        elif escolha == "3":
            cadastrar_time()
        elif escolha == "4":
            listar_times()
        elif escolha == "5":
            cadastrar_jogo()
        elif escolha == "6":
            listar_jogos()
        elif escolha == "7":
            registrar_partida()
        elif escolha == "8":
            listar_partidas()
        elif escolha == "0":
            print("Saindo...")
            sys.exit(0)
        else:
            print("Opção inválida!")

        pausar()

if __name__ == "__main__":
    menu()
