# init_db.py

import sqlite3
import os

# Caminho para o banco de dados
DB_PATH = os.path.join("db", "torneio.db")

# Garante que a pasta 'db/' exista
os.makedirs("db", exist_ok=True)

def create_tables():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    try:
        # Tabela jogador
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jogador (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                nickname TEXT UNIQUE
            );
        """)

        # Tabela time
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS time (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            );
        """)

        # Tabela jogador_time (relacionamento N:N)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jogador_time (
                jogador_id INTEGER,
                time_id INTEGER,
                FOREIGN KEY (jogador_id) REFERENCES jogador(id),
                FOREIGN KEY (time_id) REFERENCES time(id)
            );
        """)

        # Tabela jogo
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jogo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT
            );
        """)

        # Tabela partida
        cursor.execute("""
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
        """)

        connection.commit()
        print("Banco de dados criado com sucesso em:", DB_PATH)

    except sqlite3.Error as e:
        print("Erro ao criar tabelas:", e)

    finally:
        connection.close()

if __name__ == "__main__":
    create_tables()
