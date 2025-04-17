import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import textwrap
import random
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

# =============================================================================
# SISTEMA BANCÁRIO (CLASSES)
# =============================================================================

ROOT_PATH = Path(__file__).parent if "__file__" in globals() else Path(".")

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            texto = f"""\n
Agência:\t{conta.agencia}
Número:\t\t{conta.numero}
Titular:\t{conta.cliente.nome}
Saldo:\t\tR$ {conta.saldo:.2f}"""
            return texto
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\nArr! Ultrapassaste o limite de transações para hoje!")
            return False
        return transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.nome}', '{self.cpf}')>"

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        if valor > saldo:
            print("\nArr! Saldo insuficiente para essa empreitada!")
            return False
        elif valor > 0:
            self._saldo -= valor
            print("\nYo-ho-ho! Saque efetuado com sucesso!")
            return True
        else:
            print("\nArr! Valor inválido, marujo!")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nYo-ho-ho! Depósito realizado com sucesso!")
            return True
        else:
            print("\nArr! Valor inválido para depósito!")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        if valor > self._limite:
            print("\nArr! O saque excede o limite do baú!")
            return False
        elif numero_saques >= self._limite_saques:
            print("\nArr! Já usaste todos os saques permitidos, marujo!")
            return False
        else:
            return super().sacar(valor)

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"

    def __str__(self):
        return f"""\n
Agência:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente.nome}"""

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S"),
        })

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        return sucesso_transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        return sucesso_transacao

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        with open(ROOT_PATH / "log.txt", "a") as arquivo:
            arquivo.write(
                f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. Retornou {resultado}\n"
            )
        return resultado
    return envelope

def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nArr! Este cliente não tem conta no nosso navio!")
        return None
    return cliente.contas[0]

# =============================================================================
# INTERFACE PIRATA (TKINTER)
# =============================================================================

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("O Grande banco")
        self.geometry("800x600")
        self.resizable(False, False)

        # Cores e fonte com estilo pirata
        self.bg_color = "#3e2723"       # marrom escuro, como madeira envelhecida
        self.fg_color = "#fbe9e7"       # tom de pergaminho
        self.accent_color = "#ffab00"   # ouro velho
        # Tente usar uma fonte com estilo "Old English" se disponível; caso contrário, Courier
        self.font_pirate = ("Courier", 12, "bold")
        self.configure(bg=self.bg_color)

        # Listas de clientes e contas
        self.clientes = []
        self.contas = []

        # Cria um canvas de fundo com animação de caveiras flutuantes
        self.canvas = tk.Canvas(self, width=800, height=600, bg=self.bg_color, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Cria caveiras (texto com emoji ☠️) flutuantes
        self.skulls = []
        self.num_skulls = 30
        for _ in range(self.num_skulls):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            speed = random.uniform(0.5, 2.0)
            skull_id = self.canvas.create_text(x, y, text="☠️", fill=self.accent_color, font=self.font_pirate)
            self.skulls.append({"id": skull_id, "speed": speed})
        
        # Cria um frame para comportar o Notebook (com fundo semi-transparente)
        self.frame_ui = tk.Frame(self.canvas, bg=self.bg_color)
        self.canvas.create_window(0, 0, anchor="nw", window=self.frame_ui, width=800, height=600)

        # Título pirata
        titulo = tk.Label(self.frame_ui, text="Bem-vindo ao Grande banco", 
                          bg=self.bg_color, fg=self.accent_color, font=("Courier", 20, "bold"))
        titulo.pack(pady=10)

        # Configuração do Notebook com abas
        self.notebook = ttk.Notebook(self.frame_ui)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=10)

        # Aba de Operações
        self.frame_operacoes = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.frame_operacoes, text="Operações")

        # Aba de Clientes/Contas
        self.frame_clientes_contas = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(self.frame_clientes_contas, text="Clientes/Contas")

        self.estilizar_widgets()
        self.criar_widgets_operacoes()
        self.criar_widgets_clientes_contas()

        # Inicia a animação das caveiras
        self.animate_skulls()

    def estilizar_widgets(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TButton",
                        background=self.accent_color,
                        foreground="black",
                        font=self.font_pirate,
                        padding=5)
        style.map("TButton", background=[("active", "#ffd54f")])
        style.configure("TLabel", background=self.bg_color, foreground=self.fg_color, font=self.font_pirate)
        style.configure("TNotebook", background=self.bg_color)
        style.configure("TNotebook.Tab", background=self.accent_color, foreground="black", font=self.font_pirate)

    # ==================== Animação de Caveiras ====================
    def animate_skulls(self):
        for skull in self.skulls:
            # Move cada caveira para baixo de acordo com sua velocidade
            self.canvas.move(skull["id"], 0, skull["speed"])
            coords = self.canvas.coords(skull["id"])
            if coords and coords[1] > 600:
                new_x = random.randint(0, 800)
                skull["speed"] = random.uniform(0.5, 2.0)
                self.canvas.coords(skull["id"], new_x, -10)
        self.after(50, self.animate_skulls)

    # ==================== Aba Operações ====================
    def criar_widgets_operacoes(self):
        btn_depositar = ttk.Button(self.frame_operacoes, text="Depósito", command=self.janela_depositar)
        btn_depositar.pack(pady=10, ipadx=10, ipady=5)

        btn_sacar = ttk.Button(self.frame_operacoes, text="Saque", command=self.janela_sacar)
        btn_sacar.pack(pady=10, ipadx=10, ipady=5)

        btn_extrato = ttk.Button(self.frame_operacoes, text="Extrato", command=self.janela_extrato)
        btn_extrato.pack(pady=10, ipadx=10, ipady=5)

        btn_sair = ttk.Button(self.frame_operacoes, text="Abandonar Navio", command=self.destroy)
        btn_sair.pack(pady=20, ipadx=10, ipady=5)

    # ==================== Aba Clientes/Contas ====================
    def criar_widgets_clientes_contas(self):
        btn_novo_cliente = ttk.Button(self.frame_clientes_contas, text="Novo Marujo", command=self.janela_novo_cliente)
        btn_novo_cliente.pack(pady=10, ipadx=10, ipady=5)

        btn_nova_conta = ttk.Button(self.frame_clientes_contas, text="Nova Conta", command=self.janela_nova_conta)
        btn_nova_conta.pack(pady=10, ipadx=10, ipady=5)

        btn_listar_contas = ttk.Button(self.frame_clientes_contas, text="Listar Contas", command=self.janela_listar_contas)
        btn_listar_contas.pack(pady=10, ipadx=10, ipady=5)

    # ==================== Janela para Depósito ====================
    def janela_depositar(self):
        win = tk.Toplevel(self)
        win.title("Depósito")
        win.geometry("400x250")
        win.resizable(False, False)
        win.configure(bg=self.bg_color)

        lbl_cpf = ttk.Label(win, text="CPF do Marujo:")
        lbl_cpf.pack(pady=5)
        ent_cpf = ttk.Entry(win)
        ent_cpf.pack(pady=5)

        lbl_valor = ttk.Label(win, text="Valor do Tesouro:")
        lbl_valor.pack(pady=5)
        ent_valor = ttk.Entry(win)
        ent_valor.pack(pady=5)

        def confirmar_deposito():
            cpf = ent_cpf.get().strip()
            try:
                valor = float(ent_valor.get())
            except ValueError:
                messagebox.showerror("Arr!", "Valor inválido, marujo!")
                return

            cliente = filtrar_cliente(cpf, self.clientes)
            if not cliente:
                messagebox.showerror("Arr!", "Marujo não encontrado!")
                return

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                messagebox.showerror("Arr!", "Este marujo não tem conta no navio!")
                return

            transacao = Deposito(valor)
            sucesso = cliente.realizar_transacao(conta, transacao)
            if sucesso:
                messagebox.showinfo("Yo-ho-ho!", "Depósito efetuado com sucesso!")
            else:
                messagebox.showerror("Arr!", "Falha no depósito, tente de novo!")
            win.destroy()

        btn_confirmar = ttk.Button(win, text="Confirmar", command=confirmar_deposito)
        btn_confirmar.pack(pady=15, ipadx=10, ipady=5)

    # ==================== Janela para Saque ====================
    def janela_sacar(self):
        win = tk.Toplevel(self)
        win.title("Saque")
        win.geometry("400x250")
        win.resizable(False, False)
        win.configure(bg=self.bg_color)

        lbl_cpf = ttk.Label(win, text="CPF do Marujo:")
        lbl_cpf.pack(pady=5)
        ent_cpf = ttk.Entry(win)
        ent_cpf.pack(pady=5)

        lbl_valor = ttk.Label(win, text="Valor a Saquear:")
        lbl_valor.pack(pady=5)
        ent_valor = ttk.Entry(win)
        ent_valor.pack(pady=5)

        def confirmar_saque():
            cpf = ent_cpf.get().strip()
            try:
                valor = float(ent_valor.get())
            except ValueError:
                messagebox.showerror("Arr!", "Valor inválido!")
                return

            cliente = filtrar_cliente(cpf, self.clientes)
            if not cliente:
                messagebox.showerror("Arr!", "Marujo não encontrado!")
                return

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                messagebox.showerror("Arr!", "Marujo sem conta no navio!")
                return

            transacao = Saque(valor)
            sucesso = cliente.realizar_transacao(conta, transacao)
            if sucesso:
                messagebox.showinfo("Yo-ho-ho!", "Saque efetuado com sucesso!")
            else:
                messagebox.showerror("Arr!", "Falha no saque, tente de novo!")
            win.destroy()

        btn_confirmar = ttk.Button(win, text="Confirmar", command=confirmar_saque)
        btn_confirmar.pack(pady=15, ipadx=10, ipady=5)

    # ==================== Janela para Extrato ====================
    def janela_extrato(self):
        win = tk.Toplevel(self)
        win.title("Extrato")
        win.geometry("500x400")
        win.resizable(False, False)
        win.configure(bg=self.bg_color)

        lbl_cpf = ttk.Label(win, text="Informe o CPF do Marujo:")
        lbl_cpf.pack(pady=5)
        ent_cpf = ttk.Entry(win)
        ent_cpf.pack(pady=5)

        txt_extrato = scrolledtext.ScrolledText(win, width=58, height=15, bg="#5d4037", fg="white", font=self.font_pirate)
        txt_extrato.pack(pady=10)

        def buscar_extrato():
            cpf = ent_cpf.get().strip()
            cliente = filtrar_cliente(cpf, self.clientes)
            if not cliente:
                messagebox.showerror("Arr!", "Marujo não encontrado!")
                return

            conta = recuperar_conta_cliente(cliente)
            if not conta:
                messagebox.showerror("Arr!", "Marujo sem conta no navio!")
                return

            txt_extrato.delete("1.0", tk.END)
            txt_extrato.insert(tk.END, "========== EXTRATO DO TESOURO ==========\n")
            tem_transacao = False
            for transacao in conta.historico.gerar_relatorio():
                tem_transacao = True
                txt_extrato.insert(tk.END, f"{transacao['data']}\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n\n")
            if not tem_transacao:
                txt_extrato.insert(tk.END, "Nenhuma movimentação registrada nos sete mares.\n")
            txt_extrato.insert(tk.END, f"\nSaldo: R$ {conta.saldo:.2f}\n")
            txt_extrato.insert(tk.END, "==========================================")
        btn_buscar = ttk.Button(win, text="Buscar", command=buscar_extrato)
        btn_buscar.pack(pady=5, ipadx=10, ipady=5)

    # ==================== Janela para Novo Cliente ====================
    def janela_novo_cliente(self):
        win = tk.Toplevel(self)
        win.title("Novo Marujo")
        win.geometry("400x350")
        win.resizable(False, False)
        win.configure(bg=self.bg_color)

        lbl_cpf = ttk.Label(win, text="CPF (somente números):")
        lbl_cpf.pack(pady=5)
        ent_cpf = ttk.Entry(win)
        ent_cpf.pack(pady=5)

        lbl_nome = ttk.Label(win, text="Nome do Marujo:")
        lbl_nome.pack(pady=5)
        ent_nome = ttk.Entry(win)
        ent_nome.pack(pady=5)

        lbl_nasc = ttk.Label(win, text="Data de Nascimento (dd-mm-aaaa):")
        lbl_nasc.pack(pady=5)
        ent_nasc = ttk.Entry(win)
        ent_nasc.pack(pady=5)

        lbl_end = ttk.Label(win, text="Endereço (rua, nro - bairro - cidade/UF):")
        lbl_end.pack(pady=5)
        ent_end = ttk.Entry(win)
        ent_end.pack(pady=5)

        def confirmar_cliente():
            cpf = ent_cpf.get().strip()
            if filtrar_cliente(cpf, self.clientes):
                messagebox.showerror("Arr!", "Já existe um marujo com esse CPF!")
                return
            nome = ent_nome.get().strip()
            data_nascimento = ent_nasc.get().strip()
            endereco = ent_end.get().strip()

            cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
            self.clientes.append(cliente)
            messagebox.showinfo("Yo-ho-ho!", "Marujo cadastrado com sucesso!")
            win.destroy()

        btn_confirmar = ttk.Button(win, text="Confirmar", command=confirmar_cliente)
        btn_confirmar.pack(pady=15, ipadx=10, ipady=5)

    # ==================== Janela para Nova Conta ====================
    def janela_nova_conta(self):
        win = tk.Toplevel(self)
        win.title("Nova Conta")
        win.geometry("400x250")
        win.resizable(False, False)
        win.configure(bg=self.bg_color)

        lbl_cpf = ttk.Label(win, text="CPF do Marujo:")
        lbl_cpf.pack(pady=5)
        ent_cpf = ttk.Entry(win)
        ent_cpf.pack(pady=5)

        def confirmar_conta():
            cpf = ent_cpf.get().strip()
            cliente = filtrar_cliente(cpf, self.clientes)
            if not cliente:
                messagebox.showerror("Arr!", "Marujo não encontrado!")
                return

            numero_conta = len(self.contas) + 1
            conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)
            self.contas.append(conta)
            cliente.adicionar_conta(conta)
            messagebox.showinfo("Yo-ho-ho!", f"Conta criada com sucesso!\nNúmero da Conta: {numero_conta}")
            win.destroy()

        btn_confirmar = ttk.Button(win, text="Confirmar", command=confirmar_conta)
        btn_confirmar.pack(pady=15, ipadx=10, ipady=5)

    # ==================== Janela para Listar Contas ====================
    def janela_listar_contas(self):
        win = tk.Toplevel(self)
        win.title("Listar Contas")
        win.geometry("500x400")
        win.resizable(False, False)
        win.configure(bg=self.bg_color)

        txt_contas = scrolledtext.ScrolledText(win, width=60, height=20, bg="#5d4037", fg="white", font=self.font_pirate)
        txt_contas.pack(pady=10, padx=10)

        if not self.contas:
            txt_contas.insert(tk.END, "Nenhuma conta cadastrada no navio.")
        else:
            for conta_info in ContasIterador(self.contas):
                txt_contas.insert(tk.END, "=" * 50 + "\n")
                txt_contas.insert(tk.END, textwrap.dedent(conta_info) + "\n")

if __name__ == '__main__':
    app = BankApp()
    app.mainloop()
