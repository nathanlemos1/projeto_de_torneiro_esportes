import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

DB_PATH = os.path.join("db", "torneio.db")

# ======================= DB =======================
def conectar():
    return sqlite3.connect(DB_PATH)

def cadastrar_jogador(nome, idade, nickname):
    if not nome or not idade or not nickname:
        messagebox.showwarning("Campos vazios", "Preencha todos os campos!")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Idade inválida", "A idade deve ser um número inteiro.")
        return

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO jogador (nome, idade, nickname) VALUES (?, ?, ?)", (nome, idade, nickname))
        conn.commit()
        messagebox.showinfo("Sucesso", "Jogador cadastrado com sucesso!")
        atualizar_lista_jogadores()
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Nickname já existe!")
    finally:
        conn.close()

def listar_jogadores_com_times():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT j.id, j.nome, j.idade, j.nickname, COALESCE(t.nome, 'Sem time')
        FROM jogador j
        LEFT JOIN jogador_time jt ON j.id = jt.jogador_id
        LEFT JOIN time t ON jt.time_id = t.id
    """)
    jogadores = cursor.fetchall()
    conn.close()
    return jogadores

def listar_times():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM time")
    times = cursor.fetchall()
    conn.close()
    return times

def cadastrar_time(nome):
    if not nome:
        messagebox.showwarning("Campo vazio", "Informe o nome do time.")
        return

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO time (nome) VALUES (?)", (nome,))
        conn.commit()
        messagebox.showinfo("Sucesso", "Time cadastrado com sucesso!")
        atualizar_lista_times()
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Erro ao cadastrar time!")
    finally:
        conn.close()

def adicionar_jogador_ao_time(jogador_id, time_id):
    try:
        jogador_id = int(jogador_id)
        time_id = int(time_id)
    except ValueError:
        messagebox.showerror("Erro", "IDs devem ser números inteiros.")
        return

    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO jogador_time (jogador_id, time_id) VALUES (?, ?)", (jogador_id, time_id))
        conn.commit()
        messagebox.showinfo("Sucesso", f"Jogador {jogador_id} adicionado ao time {time_id}.")
        atualizar_lista_jogadores()
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Este jogador já está neste time ou os IDs não existem!")
    finally:
        conn.close()

# ======================= GUI =======================
janela = tk.Tk()
janela.title("Sistema de Torneios de eSports")
janela.geometry("750x600")
janela.configure(bg="#f0f2f5")

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background="#f0f2f5", borderwidth=0)
style.configure("TNotebook.Tab", background="#d0d7de", padding=10, font=("Arial", 10, "bold"))
style.configure("TLabelFrame", background="#ffffff", padding=10)
style.configure("TLabel", background="#ffffff")
style.configure("Treeview", font=("Arial", 10))
style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

abas = ttk.Notebook(janela)
aba_jogadores = ttk.Frame(abas)
aba_times = ttk.Frame(abas)
aba_vinculo = ttk.Frame(abas)
abas.add(aba_jogadores, text="Jogadores")
abas.add(aba_times, text="Times")
abas.add(aba_vinculo, text="Vincular Jogador ao Time")
abas.pack(expand=1, fill="both")

# ========== Aba Jogadores ==========
frame_form_jogador = ttk.LabelFrame(aba_jogadores, text="Cadastrar Jogador")
frame_form_jogador.pack(fill="x", padx=10, pady=10)

tk.Label(frame_form_jogador, text="Nome:").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(frame_form_jogador)
entry_nome.grid(row=0, column=1, sticky="ew")

tk.Label(frame_form_jogador, text="Idade:").grid(row=1, column=0, sticky="w")
entry_idade = tk.Entry(frame_form_jogador)
entry_idade.grid(row=1, column=1, sticky="ew")

tk.Label(frame_form_jogador, text="Nickname:").grid(row=2, column=0, sticky="w")
entry_nickname = tk.Entry(frame_form_jogador)
entry_nickname.grid(row=2, column=1, sticky="ew")

frame_form_jogador.columnconfigure(1, weight=1)

tk.Button(frame_form_jogador, text="Cadastrar", bg="#4caf50", fg="white", command=lambda: cadastrar_jogador(entry_nome.get(), entry_idade.get(), entry_nickname.get())).grid(row=3, column=0, columnspan=2, pady=10)

frame_lista_jogadores = ttk.LabelFrame(aba_jogadores, text="Jogadores Cadastrados")
frame_lista_jogadores.pack(fill="both", expand=True, padx=10, pady=10)

tree_jogadores = ttk.Treeview(frame_lista_jogadores, columns=("ID", "Nome", "Idade", "Nickname", "Time"), show="headings")
tree_jogadores.heading("ID", text="ID")
tree_jogadores.heading("Nome", text="Nome")
tree_jogadores.heading("Idade", text="Idade")
tree_jogadores.heading("Nickname", text="Nickname")
tree_jogadores.heading("Time", text="Time")
tree_jogadores.pack(fill="both", expand=True)

def atualizar_lista_jogadores():
    for item in tree_jogadores.get_children():
        tree_jogadores.delete(item)
    for jogador in listar_jogadores_com_times():
        tree_jogadores.insert("", tk.END, values=jogador)

# ========== Aba Times ==========
frame_form_time = ttk.LabelFrame(aba_times, text="Cadastrar Time")
frame_form_time.pack(fill="x", padx=10, pady=10)

tk.Label(frame_form_time, text="Nome do Time:").grid(row=0, column=0, sticky="w")
entry_nome_time = tk.Entry(frame_form_time)
entry_nome_time.grid(row=0, column=1, sticky="ew")

frame_form_time.columnconfigure(1, weight=1)

tk.Button(frame_form_time, text="Cadastrar Time", bg="#2196f3", fg="white", command=lambda: cadastrar_time(entry_nome_time.get())).grid(row=1, column=0, columnspan=2, pady=10)

frame_lista_times = ttk.LabelFrame(aba_times, text="Times Cadastrados")
frame_lista_times.pack(fill="both", expand=True, padx=10, pady=10)

tree_times = ttk.Treeview(frame_lista_times, columns=("ID", "Nome"), show="headings")
tree_times.heading("ID", text="ID")
tree_times.heading("Nome", text="Nome")
tree_times.pack(fill="both", expand=True)

def atualizar_lista_times():
    for item in tree_times.get_children():
        tree_times.delete(item)
    for time in listar_times():
        tree_times.insert("", tk.END, values=time)

# ========== Aba Vincular Jogador ao Time ==========
frame_vinculo = ttk.LabelFrame(aba_vinculo, text="Adicionar Jogador ao Time")
frame_vinculo.pack(fill="x", padx=10, pady=10)

tk.Label(frame_vinculo, text="ID do Jogador:").grid(row=0, column=0, sticky="w")
entry_jogador_id = tk.Entry(frame_vinculo)
entry_jogador_id.grid(row=0, column=1, sticky="ew")

tk.Label(frame_vinculo, text="ID do Time:").grid(row=1, column=0, sticky="w")
entry_time_id = tk.Entry(frame_vinculo)
entry_time_id.grid(row=1, column=1, sticky="ew")

frame_vinculo.columnconfigure(1, weight=1)

tk.Button(frame_vinculo, text="Adicionar", bg="#ff9800", fg="white", command=lambda: adicionar_jogador_ao_time(entry_jogador_id.get(), entry_time_id.get())).grid(row=2, column=0, columnspan=2, pady=10)

# Inicialização de listas
atualizar_lista_jogadores()
atualizar_lista_times()

janela.mainloop()
