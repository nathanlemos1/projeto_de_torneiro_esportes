# utils.py

def input_inteiro(msg, minimo=None, maximo=None):
    """
    Solicita ao usuário um número inteiro, com validação opcional de intervalo.
    """
    while True:
        try:
            valor = int(input(msg))
            if (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
                print(f"Digite um número entre {minimo} e {maximo}.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


def input_texto(msg, obrigatorio=True):
    """
    Solicita ao usuário uma string de texto.
    """
    while True:
        texto = input(msg).strip()
        if obrigatorio and texto == "":
            print("Este campo é obrigatório.")
        else:
            return texto


def pausar():
    """
    Pausa a execução até o usuário pressionar Enter.
    """
    input("\nPressione Enter para continuar...")


def exibir_titulo(titulo):
    """
    Exibe um título formatado.
    """
    print("\n" + "=" * len(titulo))
    print(titulo.upper())
    print("=" * len(titulo))
