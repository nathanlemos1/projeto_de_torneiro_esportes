# src/utils.py

import os

def limpar_tela():
    """
    Limpa o terminal, compatível com Windows e Unix.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    """
    Pausa a execução até que o usuário pressione Enter.
    """
    input("\nPressione Enter para continuar...")


def ler_inteiro(mensagem, minimo=None, maximo=None):
    """
    Lê um número inteiro com validação opcional de faixa.
    """
    while True:
        try:
            valor = int(input(mensagem))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"Por favor, insira um número entre {minimo} e {maximo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_texto(mensagem, obrigatorio=True):
    """
    Lê um texto com a opção de exigir que não esteja vazio.
    """
    while True:
        texto = input(mensagem).strip()
        if obrigatorio and not texto:
            print("Este campo é obrigatório.")
        else:
            return texto
