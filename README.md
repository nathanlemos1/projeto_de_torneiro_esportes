# 🕹️ Sistema de Torneios de eSports com Tkinter e SQLite

Este projeto é um sistema desktop de gerenciamento de torneios de eSports, desenvolvido em **Python**, utilizando **Tkinter** para a interface gráfica e **SQLite** para armazenamento local de dados.

---

## 📌 Objetivo do Projeto

O objetivo deste sistema é fornecer uma plataforma simples onde seja possível:

- Cadastrar jogadores e times
- Associar jogadores a times
- Visualizar os jogadores cadastrados e a qual time cada um pertence
- Realizar tudo isso com uma interface intuitiva e funcional

Este projeto serve como uma ótima base para quem está aprendendo **programação com interface gráfica (GUI)** e **banco de dados relacional** com Python.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter**: biblioteca padrão do Python para criação de interfaces gráficas
- **SQLite**: banco de dados relacional leve e integrado ao Python
- **ttk (Themed Tkinter Widgets)**: usado para criar uma interface moderna e amigável

---

## 📋 Funcionalidades Implementadas

### ✅ Cadastro de Jogadores
O formulário de cadastro exige:
- Nome
- Idade (número inteiro)
- Nickname (único)

Caso algum campo esteja vazio ou a idade não seja válida, uma mensagem de erro é exibida.

### ✅ Cadastro de Times
Permite cadastrar o nome do time. O nome não precisa ser único, mas pode ser estendido.

### ✅ Vinculação de Jogador a um Time
É possível associar um jogador a um time existente, informando os **IDs** correspondentes.

Essa operação é registrada na tabela intermediária `jogador_time`, simulando um relacionamento muitos-para-muitos (apesar de, no código atual, cada jogador só poder estar em um time).

### ✅ Exibição em Tabelas (Treeview)
As informações são apresentadas de forma clara por meio de tabelas:
- Jogadores com ID, nome, idade, nickname e time atual
- Times com ID e nome

Essas tabelas são atualizadas automaticamente após cada ação (cadastro ou vínculo).

---

## 🧠 Estrutura Interna do Código

### 📁 Organização por Abas
A interface gráfica é organizada em **3 abas**:
- **Jogadores**: formulário de cadastro + listagem
- **Times**: formulário de cadastro + listagem
- **Vincular**: campos para vincular jogador a time

As abas foram criadas com o widget `ttk.Notebook`, permitindo alternar entre funcionalidades de forma intuitiva.

### 🧩 Componentes da Interface
- `Entry`: campos de entrada de texto
- `Treeview`: exibição em forma de tabela
- `LabelFrame`: organização de blocos de formulários
- `Button`: execução de ações
- `messagebox`: exibição de mensagens de erro/sucesso

### 🎨 Estilização
O sistema utiliza o tema `clam` do `ttk.Style` e define cores, fontes e espaçamentos para tornar a experiência visual mais agradável e moderna.

---

## 🗃️ Banco de Dados (SQLite)

O banco de dados é um arquivo local SQLite (`torneio.db`) armazenado na pasta `db/`. Ele é acessado por meio da função `conectar()` que abre a conexão com o caminho configurado.

### 📌 Tabelas:

#### `jogador`
- `id`: chave primária
- `nome`: nome do jogador
- `idade`: idade (inteiro)
- `nickname`: identificador único

#### `time`
- `id`: chave primária
- `nome`: nome do time

#### `jogador_time`
- `jogador_id`: chave estrangeira para `jogador`
- `time_id`: chave estrangeira para `time`
- `PRIMARY KEY (jogador_id)`: garante que um jogador só esteja em um time

O uso da cláusula `LEFT JOIN` na listagem de jogadores permite que jogadores sem time ainda sejam exibidos como "Sem time".

---

## 🔄 Atualização Dinâmica

Após cada operação (cadastro ou associação), as tabelas (`Treeview`) são automaticamente atualizadas chamando:

- `atualizar_lista_jogadores()`
- `atualizar_lista_times()`

Essas funções removem todos os dados antigos e reinserem os atualizados diretamente do banco de dados, garantindo sincronia da interface com o banco.

---

## ✅ Requisitos para Executar

### `requirements.txt`

```txt
```
---

### Autor: Nathan Lemos