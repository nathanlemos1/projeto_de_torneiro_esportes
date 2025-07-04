import sqlite3
import os

# ========== CONFIGURAÇÃO DO BANCO ==========
DB_PATH = os.path.join("db", "torneio.db")

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabelas():
    os.makedirs("db", exist_ok=True)
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            nickname TEXT UNIQUE
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS time (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogador_time (
            jogador_id INTEGER,
            time_id INTEGER,
            FOREIGN KEY (jogador_id) REFERENCES jogador(id),
            FOREIGN KEY (time_id) REFERENCES time(id)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jogo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS partida (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time1_id INTEGER,
            time2_id INTEGER,
            jogo_id INTEGER,
            data TEXT,
            vencedor_id INTEGER,
            FOREIGN KEY (time1_id) REFERENCES time(id),
            FOREIGN KEY (time2_id) REFERENCES time(id),
            FOREIGN KEY (jogo_id) REFERENCES jogo(id),
            FOREIGN KEY (vencedor_id) REFERENCES time(id)
        );
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso!")


# ========== FUNÇÕES UTILITÁRIAS ==========

def input_inteiro(msg, minimo=None, maximo=None):
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
    while True:
        texto = input(msg).strip()
        if obrigatorio and texto == "":
            print("Este campo é obrigatório.")
        else:
            return texto

def pausar():
    input("\nPressione Enter para continuar...")

def exibir_titulo(titulo):
    print("\n" + "=" * len(titulo))
    print(titulo.upper())
    print("=" * len(titulo))


# ========== CRUD - Jogadores ==========

def adicionar_jogador(nome, idade, nickname):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO jogador (nome, idade, nickname) VALUES (?, ?, ?)",
            (nome, idade, nickname)
        )
        conn.commit()
        print("Jogador cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: nickname já existe!")
    except Exception as e:
        print(f"Erro ao adicionar jogador: {e}")
    finally:
        conn.close()

def listar_jogadores():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, idade, nickname FROM jogador")
        jogadores = cursor.fetchall()

        if jogadores:
            print("\nLista de Jogadores:")
            for j in jogadores:
                print(f"ID: {j[0]} | Nome: {j[1]} | Idade: {j[2]} | Nickname: {j[3]}")
        else:
            print("Nenhum jogador cadastrado.")
    except Exception as e:
        print(f"Erro ao listar jogadores: {e}")
    finally:
        conn.close()


# ========== MENUS ==========

def menu_jogadores():
    while True:
        exibir_titulo("Gerenciar Jogadores")
        print("1. Cadastrar jogador")
        print("2. Listar jogadores")
        print("0. Voltar")

        opcao = input_inteiro("Escolha uma opção: ", 0, 2)

        if opcao == 1:
            nome = input_texto("Nome: ")
            idade = input_inteiro("Idade: ")
            nickname = input_texto("Nickname: ")
            adicionar_jogador(nome, idade, nickname)
            pausar()
        elif opcao == 2:
            listar_jogadores()
            pausar()
        elif opcao == 0:
            break

def menu_principal():
    while True:
        exibir_titulo("Sistema de Torneios de eSports")
        print("1. Gerenciar Jogadores")
        print("2. Gerenciar Times (em breve)")
        print("3. Gerenciar Jogos (em breve)")
        print("4. Gerenciar Partidas (em breve)")
        print("0. Sair")

        opcao = input_inteiro("Escolha uma opção: ", 0, 4)

        if opcao == 1:
            menu_jogadores()
        elif opcao == 0:
            print("Saindo do sistema...")
            break
        else:
            print("Funcionalidade ainda não implementada.")
            pausar()


# ========== EXECUÇÃO ==========
if __name__ == "__main__":
    criar_tabelas()
    menu_principal()
