# src/gui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

DB_PATH = "db/torneio.db"


def conectar():
    return sqlite3.connect(DB_PATH)


# ---------- Funções de ações ----------

def cadastrar_jogador():
    nome = simpledialog.askstring("Cadastro de Jogador", "Nome:")
    idade = simpledialog.askinteger("Cadastro de Jogador", "Idade:")
    nickname = simpledialog.askstring("Cadastro de Jogador", "Nickname:")

    if not nome or not nickname:
        messagebox.showerror("Erro", "Nome e nickname são obrigatórios!")
        return

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jogador (nome, idade, nickname) VALUES (?, ?, ?)", (nome, idade, nickname))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Jogador cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Nickname já existe!")


def listar_jogadores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, idade, nickname FROM jogador")
    jogadores = cursor.fetchall()
    conn.close()

    if jogadores:
        texto = "\n".join([f"{j[0]} ({j[1]} anos) - Nick: {j[2]}" for j in jogadores])
    else:
        texto = "Nenhum jogador encontrado."

    messagebox.showinfo("Jogadores", texto)


def cadastrar_jogo():
    nome = simpledialog.askstring("Cadastro de Jogo", "Nome do Jogo:")
    categoria = simpledialog.askstring("Cadastro de Jogo", "Categoria (FPS, MOBA, etc):")

    if not nome:
        messagebox.showerror("Erro", "Nome do jogo é obrigatório!")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jogo (nome, categoria) VALUES (?, ?)", (nome, categoria))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Jogo cadastrado com sucesso!")


def listar_jogos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, categoria FROM jogo")
    jogos = cursor.fetchall()
    conn.close()

    if jogos:
        texto = "\n".join([f"{j[0]} [{j[1]}]" for j in jogos])
    else:
        texto = "Nenhum jogo cadastrado."

    messagebox.showinfo("Jogos", texto)


# ---------- GUI Principal ----------

def iniciar_gui():
    root = tk.Tk()
    root.title("Sistema de Torneio de eSports")
    root.geometry("400x400")

    titulo = tk.Label(root, text="Sistema de Torneio de eSports", font=("Helvetica", 16))
    titulo.pack(pady=20)

    # Botões principais
    tk.Button(root, text="Cadastrar Jogador", command=cadastrar_jogador, width=30).pack(pady=5)
    tk.Button(root, text="Listar Jogadores", command=listar_jogadores, width=30).pack(pady=5)

    tk.Button(root, text="Cadastrar Jogo", command=cadastrar_jogo, width=30).pack(pady=5)
    tk.Button(root, text="Listar Jogos", command=listar_jogos, width=30).pack(pady=5)

    # Aqui você pode adicionar mais funcionalidades:
    # - Cadastrar/Listar Times
    # - Registrar/Listar Partidas

    tk.Button(root, text="Sair", command=root.destroy, bg="red", fg="white", width=30).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    iniciar_gui()
