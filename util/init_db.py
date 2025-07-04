# init_db.py

import sqlite3
import os

# Caminho do banco de dados
DB_PATH = os.path.join("db", "torneio.db")

def criar_tabelas():
    # Conecta ao banco de dados (cria o arquivo se não existir)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Criação das tabelas
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

    # Salva as alterações e fecha a conexão
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso!")

if __name__ == "__main__":
    # Garante que o diretório 'db/' exista
    os.makedirs("db", exist_ok=True)
    criar_tabelas()
