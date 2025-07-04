# src/db_manager.py

import sqlite3
from utils import ler_texto, ler_inteiro
from db_manager import cadastrar_jogador

DB_PATH = "db/torneio.db"


def conectar():
    return sqlite3.connect(DB_PATH)


# ----------------- Jogadores -----------------

def cadastrar_jogador():
    print("\n--- Cadastro de Jogador ---")
    nome = ler_texto("Nome: ")
    idade = ler_inteiro("Idade: ", minimo=0)
    nickname = ler_texto("Nickname: ")

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO jogador (nome, idade, nickname) VALUES (?, ?, ?)",
            (nome, idade, nickname)
        )
        conn.commit()
        print("✅ Jogador cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("❌ Nickname já existe!")
    finally:
        conn.close()


def listar_jogadores():
    print("\n--- Lista de Jogadores ---")
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, idade, nickname FROM jogador")
    jogadores = cursor.fetchall()

    if not jogadores:
        print("Nenhum jogador cadastrado.")
    else:
        for j in jogadores:
            print(f"{j[0]} - {j[1]} ({j[2]} anos) - Nick: {j[3]}")

    conn.close()


# ----------------- Times -----------------

def cadastrar_time():
    print("\n--- Cadastro de Time ---")
    nome = ler_texto("Nome do time: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO time (nome) VALUES (?)", (nome,))
    conn.commit()
    time_id = cursor.lastrowid

    print("Adicione jogadores ao time. (Digite 0 para sair)")

    while True:
        listar_jogadores()
        jogador_id = ler_inteiro("ID do jogador para adicionar ao time (0 para encerrar): ")

        if jogador_id == 0:
            break

        try:
            cursor.execute(
                "INSERT INTO jogador_time (jogador_id, time_id) VALUES (?, ?)",
                (jogador_id, time_id)
            )
            conn.commit()
            print("✅ Jogador adicionado.")
        except sqlite3.IntegrityError:
            print("❌ Este jogador já está neste time ou não existe.")

    conn.close()


def listar_times():
    print("\n--- Lista de Times ---")
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM time")
    times = cursor.fetchall()

    for t in times:
        print(f"\nTime {t[0]} - {t[1]}")
        cursor.execute("""
            SELECT j.nome, j.nickname 
            FROM jogador j
            JOIN jogador_time jt ON j.id = jt.jogador_id
            WHERE jt.time_id = ?
        """, (t[0],))
        jogadores = cursor.fetchall()

        if jogadores:
            for j in jogadores:
                print(f"   - {j[0]} (Nick: {j[1]})")
        else:
            print("   (Sem jogadores)")

    conn.close()


# ----------------- Jogos -----------------

def cadastrar_jogo():
    print("\n--- Cadastro de Jogo ---")
    nome = ler_texto("Nome do jogo: ")
    categoria = ler_texto("Categoria (FPS, MOBA, etc): ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jogo (nome, categoria) VALUES (?, ?)", (nome, categoria))
    conn.commit()
    conn.close()
    print("✅ Jogo cadastrado com sucesso!")


def listar_jogos():
    print("\n--- Lista de Jogos ---")
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, categoria FROM jogo")
    jogos = cursor.fetchall()

    for j in jogos:
        print(f"{j[0]} - {j[1]} [{j[2]}]")

    conn.close()


# ----------------- Partidas -----------------

def registrar_partida():
    print("\n--- Registro de Partida ---")
    listar_times()
    time1_id = ler_inteiro("ID do Time 1: ")
    time2_id = ler_inteiro("ID do Time 2: ")

    if time1_id == time2_id:
        print("❌ Os times não podem ser iguais.")
        return

    listar_jogos()
    jogo_id = ler_inteiro("ID do jogo: ")
    data = ler_texto("Data da partida (ex: 2025-07-04): ")
    vencedor_id = ler_inteiro("ID do time vencedor: ")

    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO partida (time1_id, time2_id, jogo_id, data, vencedor_id)
            VALUES (?, ?, ?, ?, ?)
        """, (time1_id, time2_id, jogo_id, data, vencedor_id))
        conn.commit()
        print("✅ Partida registrada com sucesso!")
    except sqlite3.IntegrityError:
        print("❌ Erro ao registrar a partida. Verifique os IDs.")
    finally:
        conn.close()


def listar_partidas():
    print("\n--- Lista de Partidas ---")
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.id, t1.nome, t2.nome, j.nome, p.data, tv.nome
        FROM partida p
        JOIN time t1 ON p.time1_id = t1.id
        JOIN time t2 ON p.time2_id = t2.id
        JOIN jogo j ON p.jogo_id = j.id
        JOIN time tv ON p.vencedor_id = tv.id
    """)
    partidas = cursor.fetchall()

    for p in partidas:
        print(f"#{p[0]} - {p[1]} vs {p[2]} | Jogo: {p[3]} | Data: {p[4]} | Vencedor: {p[5]}")

    conn.close()
