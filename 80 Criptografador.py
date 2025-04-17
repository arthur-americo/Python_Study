import os
import json
import base64
import secrets
import string
import bcrypt
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random 

# Diretórios e arquivos (armazenados na pasta de backup)
BACKUP_DIR = r"H:\My Drive\Trabalho\Coding Training\Jarvis\Criptografador"
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)
MASTER_HASH_FILE = os.path.join(BACKUP_DIR, "master.hash")
SALT_FILE = os.path.join(BACKUP_DIR, "salt.bin")
CREDENTIALS_FILE = os.path.join(BACKUP_DIR, "credentials.enc")

# Deriva a chave de criptografia a partir da senha mestra com PBKDF2HMAC
def derive_key(master_password: str) -> bytes:
    if os.path.exists(SALT_FILE):
        with open(SALT_FILE, "rb") as f:
            salt = f.read()
    else:
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

# Carrega as credenciais (descriptografando o arquivo JSON)
def load_credentials(fernet: Fernet) -> dict:
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "rb") as f:
            data = f.read()
        try:
            decrypted = fernet.decrypt(data)
            credentials = json.loads(decrypted.decode())
        except Exception as e:
            messagebox.showerror("Erro", "Falha ao decifrar o arquivo de credenciais.")
            credentials = {}
    else:
        credentials = {}
    return credentials

# Salva as credenciais no arquivo criptografado
def save_credentials(credentials: dict, fernet: Fernet) -> None:
    data = json.dumps(credentials).encode()
    encrypted = fernet.encrypt(data)
    with open(CREDENTIALS_FILE, "wb") as f:
        f.write(encrypted)

# Gera uma senha aleatória customizada
def generate_random_password(length: int = 12, use_symbols: bool = True, use_numbers: bool = True) -> str:
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Armazena a senha mestra (hash com bcrypt)
def set_master_password(master_password: str) -> None:
    hashed = bcrypt.hashpw(master_password.encode(), bcrypt.gensalt())
    with open(MASTER_HASH_FILE, "wb") as f:
        f.write(hashed)

# Verifica a senha mestra com bcrypt
def check_master_password(input_password: str) -> bool:
    if os.path.exists(MASTER_HASH_FILE):
        with open(MASTER_HASH_FILE, "rb") as f:
            stored_hash = f.read()
        return bcrypt.checkpw(input_password.encode(), stored_hash)
    else:
        return False

# Classe principal da aplicação

class PasswordManagerApp:
    def __init__(self, master: tk.Tk, fernet: Fernet):
        # Exibe a splash screen com círculo azul giratório por 5 segundos
        self.show_splash(master)

        self.master = master
        self.fernet = fernet
        self.master.title("J.A.R.V.I.S.")
        self.master.geometry("1600x1200")
        self.master.configure(bg="#2E2E2E")

        # Define fonte moderna para toda a aplicação
        default_font = ("Segoe UI", 10)
        self.master.option_add("*Font", default_font)

        # Carrega as credenciais já salvas
        self.credentials = load_credentials(self.fernet)

        # Configuração de estilos modernos inspirados na interface da Steam
        style = ttk.Style(self.master)
        style.theme_use("clam")

        # Personalização das abas com fundo azul e cantos arredondados
        style.configure("TNotebook", background="#2E2E2E", borderwidth=0)
        style.configure("TFrame", background="#2E2E2E")
        style.configure("TLabel", background="#2E2E2E", foreground="white")
        style.configure("TNotebook.Tab",
                        background="#3498DB",
                        foreground="white",
                        padding=[15, 5],  # Aumenta a área de clique
                        font=("Segoe UI", 12, "bold"))
        style.map("TNotebook.Tab",
                background=[("selected", "#1E90FF")],  # Azul mais vibrante na aba ativa
                foreground=[("selected", "white")])

        # Bordas arredondadas nas abas
        style.layout("TNotebook.Tab", [
            ("Notebook.tab", {"sticky": "nswe", "children": [
                ("Notebook.padding", {"side": "top", "sticky": "nswe", "children": [
                    ("Notebook.label", {"side": "top", "sticky": ""})
                ]})
            ]})
        ])

        # Animação suave ao alternar abas
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        self.notebook.bind("<<NotebookTabChanged>>", self.animate_tab_switch)

        # Estilo para os botões arredondados e modernos
        style.configure("Rounded.TButton",
                        background="#3a7ebf",
                        foreground="white",
                        borderwidth=0,
                        relief="flat",
                        padding=12)
        style.map("Rounded.TButton",
                background=[("active", "#2980B9")],
                relief=[("pressed", "sunken")])

        # Estilo para o Treeview
        style.configure("Treeview",
                        background="#1C1C1C",
                        foreground="white",
                        fieldbackground="#1C1C1C",
                        rowheight=30)

        # Cria as abas com as funcionalidades
        self.create_add_tab()
        self.create_search_tab()
        self.create_generate_tab()
        self.create_list_tab()


    
    # Exibe a splash screen com um círculo azul giratório
    def show_splash(self, master):
        master.withdraw()
        splash = tk.Toplevel(master)
        splash.overrideredirect(True)
        
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        splash.geometry(f"{screen_width}x{screen_height}+0+0")
        splash.configure(bg="#0A0E14")  # Azul muito escuro
        
        canvas = tk.Canvas(splash, width=screen_width, height=screen_height, bg="#0A0E14", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Cores do espectro azul
        BLUE_PALETTE = [
            "#001F3F",  # Azul naval
            "#003366",  # Azul profundo
            "#004080",  # Azul oceano
            "#0059B3",  # Azul vivo
            "#0074E8",  # Azul elétrico
            "#1A8CFF",  # Azul brilhante
            "#4DA6FF",  # Azul céu
            "#80BFFF"   # Azul claro
        ]
        
        center_x = screen_width // 2
        center_y = screen_height // 2
        arc_radius = min(screen_width, screen_height) // 4
        arc = canvas.create_arc(
            center_x - arc_radius, center_y - arc_radius,
            center_x + arc_radius, center_y + arc_radius,
            start=0, extent=180, 
            outline=BLUE_PALETTE[3], 
            width=15, 
            style='arc'
        )
        start_angle = 0
        
        num_particles = 100
        particles = []
        for _ in range(num_particles):
            particles.append({
                'x': random.uniform(0, screen_width),
                'y': random.uniform(0, screen_height),
                'vx': random.uniform(-2, 2),
                'vy': random.uniform(-2, 2),
                'size': random.uniform(2, 5),
                'life': random.uniform(60, 180),
                'color': random.choice(BLUE_PALETTE[2:])
            })
        
        def create_blue_gradient():
            canvas.delete("gradient")
            for i in range(100):
                intensity = i / 100
                color = f"#0000{int(255 * intensity):02x}"
                canvas.create_rectangle(
                    0, i * (screen_height/100),
                    screen_width, (i+1) * (screen_height/100),
                    fill=color, 
                    outline="", 
                    tags="gradient"
                )
        
        def update_particles():
            canvas.delete("particle")
            for p in particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['life'] -= 1
                if p['life'] <= 0 or not (0 < p['x'] < screen_width) or not (0 < p['y'] < screen_height):
                    p.update({
                        'x': random.uniform(0, screen_width),
                        'y': random.uniform(0, screen_height),
                        'life': random.uniform(60, 180)
                    })
                alpha = min(p['life'] / 100, 1)
                canvas.create_oval(
                    p['x'] - p['size'], p['y'] - p['size'],
                    p['x'] + p['size'], p['y'] + p['size'],
                    fill=p['color'], 
                    outline="", 
                    tags="particle",
                    stipple="gray50" if alpha < 0.8 else None
                )
        
        def animate():
            nonlocal start_angle
            create_blue_gradient()
            update_particles()
            start_angle = (start_angle + 3) % 360
            canvas.itemconfig(arc, start=start_angle)
            for i in range(3):
                offset = i * 30
                canvas.create_arc(
                    center_x - arc_radius - offset, center_y - arc_radius - offset,
                    center_x + arc_radius + offset, center_y + arc_radius + offset,
                    start=start_angle + offset, 
                    extent=180 - (i * 20),
                    outline=BLUE_PALETTE[i+2], 
                    width=8, 
                    style='arc',
                    tags="arcs"
                )
            splash.after(20, animate)
        
        animate()
        
        canvas.create_text(
            center_x, center_y + arc_radius + 50,
            text="INICIALIZANDO SISTEMAS",
            font=("Roboto Mono", 24, "bold"),
            fill=BLUE_PALETTE[4],
            tags="text"
        )
        
        def close_splash():
            canvas.delete("all")
            splash.destroy()
            master.deiconify()
        
        splash.after(10000, close_splash)
        master.wait_window(splash)
    
    # Animação de transição ao trocar de aba (efeito robusto com gradiente e partículas)
    def animate_tab_switch(self, event):
        current_tab = event.widget.nametowidget(event.widget.select())
        current_tab.update_idletasks()
        width = current_tab.winfo_width()
        height = current_tab.winfo_height()
        overlay = tk.Canvas(current_tab, width=width, height=height, bg="#2E2E2E", highlightthickness=0)
        overlay.place(x=0, y=0)
        
        BLUE_PALETTE = [
            "#001F3F",  # Azul naval
            "#003366",  # Azul profundo
            "#004080",  # Azul oceano
            "#0059B3",  # Azul vivo
            "#0074E8",  # Azul elétrico
            "#1A8CFF",  # Azul brilhante
            "#4DA6FF",  # Azul céu
            "#80BFFF"   # Azul claro
        ]
        
        num_particles = 50
        particles = []
        for _ in range(num_particles):
            particles.append({
                'x': random.uniform(0, width),
                'y': random.uniform(0, height),
                'vx': random.uniform(-1, 1),
                'vy': random.uniform(-3, -1),  # movimento para cima
                'size': random.uniform(2, 4),
                'life': random.uniform(30, 60),
                'color': random.choice(BLUE_PALETTE[2:])
            })
        
        offset = 0
        def update_animation():
            nonlocal offset
            overlay.delete("all")
            steps = 10
            # Cria um gradiente animado similar ao da splash, mas aplicado à transição
            for i in range(steps):
                intensity = i / steps
                color = f"#0000{int(intensity * 255):02x}"
                y1 = (height / steps) * i + offset
                y2 = (height / steps) * (i + 1) + offset
                overlay.create_rectangle(0, y1, width, y2, fill=color, outline="", tags="gradient")
            # Atualiza e desenha partículas dinâmicas
            for p in particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['life'] -= 1
                if p['life'] <= 0 or p['y'] < 0:
                    p['x'] = random.uniform(0, width)
                    p['y'] = height
                    p['life'] = random.uniform(30, 60)
                overlay.create_oval(
                    p['x'] - p['size'], p['y'] - p['size'],
                    p['x'] + p['size'], p['y'] + p['size'],
                    fill=p['color'], outline="", tags="particle"
                )
            # Efeito de slide-up: move o overlay para cima
            offset -= 10
            overlay.place_configure(y=offset)
            if offset > -height:
                current_tab.after(10, update_animation)
            else:
                overlay.destroy()
        update_animation()
    
    # Aba para adicionar nova credencial
    def create_add_tab(self):
        # Cria a aba "Adicionar Senha" no Notebook
        self.add_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.add_tab, text="Adicionar Senha")

        # --- Fundo Animado com Partículas Neon ---
        canvas_bg = tk.Canvas(self.add_tab, bg="#000000", highlightthickness=0)
        canvas_bg.pack(fill="both", expand=True)

        particles = []
        num_particles = 30
        for _ in range(num_particles):
            particles.append({
                "x": random.uniform(0, 800),
                "y": random.uniform(0, 600),
                "vx": random.uniform(-2, 2),
                "vy": random.uniform(-2, 2),
                "size": random.uniform(2, 4),
                "color": random.choice(["#00FFFF", "#00BFFF", "#1E90FF", "#40E0D0"])
            })

        def animate_particles():
            canvas_bg.delete("particle")
            w = canvas_bg.winfo_width()
            h = canvas_bg.winfo_height()
            for p in particles:
                p["x"] += p["vx"]
                p["y"] += p["vy"]
                if p["x"] < 0: p["x"] = w
                elif p["x"] > w: p["x"] = 0
                if p["y"] < 0: p["y"] = h
                elif p["y"] > h: p["y"] = 0
                canvas_bg.create_oval(
                    p["x"] - p["size"], p["y"] - p["size"],
                    p["x"] + p["size"], p["y"] + p["size"],
                    fill=p["color"], outline="", tags="particle"
                )
            canvas_bg.after(30, animate_particles)

        animate_particles()

        # --- Layout Responsivo e Centralização ---
        widget_frame = tk.Frame(canvas_bg, bg="#000000")
        window_item = canvas_bg.create_window(0, 0, window=widget_frame)

        def resize_widget_frame(event):
            w, h = event.width, event.height
            frame_width = int(w * 0.6)
            frame_height = int(h * 0.6)
            canvas_bg.itemconfig(window_item, width=frame_width, height=frame_height)
            canvas_bg.coords(window_item, w // 2, h // 2)
        canvas_bg.bind("<Configure>", resize_widget_frame)

        # --- Estilos Personalizados ---
        style = ttk.Style(self.master)
        style.configure("Add.TLabel",
                        background="#000000",
                        foreground="#00BFFF",
                        font=("Segoe UI", 20, "bold"))
        style.configure("Add.TButton",
                        background="#1E90FF",
                        foreground="white",
                        font=("Segoe UI", 20, "bold"),
                        padding=15)
        style.map("Add.TButton",
                background=[("active", "#00BFFF")])

        # --- Widgets da Interface ---
        lbl_service = ttk.Label(widget_frame, text="Serviço:", style="Add.TLabel",font=("Segoe UI", 20, "bold"))
        lbl_service.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_service = ttk.Entry(widget_frame, width=40, font=("Segoe UI", 20), justify="center")
        self.entry_service.grid(row=0, column=1, padx=10, pady=10)

        lbl_username = ttk.Label(widget_frame, text="Usuário:", style="Add.TLabel",font=("Segoe UI", 20, "bold"))
        lbl_username.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_username = ttk.Entry(widget_frame, width=40, font=("Segoe UI", 20), justify="center")
        self.entry_username.grid(row=1, column=1, padx=10, pady=10)

        lbl_password = ttk.Label(widget_frame, text="Senha:", style="Add.TLabel",font=("Segoe UI", 20, "bold"))
        lbl_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_password = ttk.Entry(widget_frame, width=40, show="*", font=("Segoe UI", 20), justify="center")
        self.entry_password.grid(row=2, column=1, padx=10, pady=10)

        btn_add = ttk.Button(widget_frame, text="Adicionar", command=self.add_credential, style="Add.TButton")
        btn_add.grid(row=3, column=0, columnspan=2, pady=20)
        btn_add.bind("<Enter>", lambda e: btn_add.configure(cursor="hand2"))
        btn_add.bind("<Leave>", lambda e: btn_add.configure(cursor=""))

        # Centraliza os widgets no frame
        widget_frame.grid_columnconfigure(0, weight=1)
        widget_frame.grid_columnconfigure(1, weight=1)


    
    def on_button_hover(self, event, widget):
        widget.configure(style="Hover.TButton")
    
    def on_button_leave(self, event, widget):
        widget.configure(style="TButton")
    
    # Aba para buscar uma credencial por serviço
    def create_search_tab(self):
        # Cria a aba "Buscar Credencial" no Notebook
        self.search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.search_tab, text="Buscar Credencial")

        # --- Fundo Animado com Partículas Neon ---
        canvas_bg = tk.Canvas(self.search_tab, bg="#000000", highlightthickness=0)
        canvas_bg.pack(fill="both", expand=True)

        particles = []
        num_particles = 30
        for _ in range(num_particles):
            particles.append({
                "x": random.uniform(0, 800),
                "y": random.uniform(0, 600),
                "vx": random.uniform(-2, 2),
                "vy": random.uniform(-2, 2),
                "size": random.uniform(2, 4),
                "color": random.choice(["#00FFFF", "#00BFFF", "#1E90FF", "#40E0D0"])
            })

        def animate_particles():
            canvas_bg.delete("particle")
            w = canvas_bg.winfo_width()
            h = canvas_bg.winfo_height()
            for p in particles:
                p["x"] += p["vx"]
                p["y"] += p["vy"]
                if p["x"] < 0: p["x"] = w
                elif p["x"] > w: p["x"] = 0
                if p["y"] < 0: p["y"] = h
                elif p["y"] > h: p["y"] = 0
                canvas_bg.create_oval(
                    p["x"] - p["size"], p["y"] - p["size"],
                    p["x"] + p["size"], p["y"] + p["size"],
                    fill=p["color"], outline="", tags="particle"
                )
            canvas_bg.after(10, animate_particles)

        animate_particles()

        # --- Layout Responsivo e Centralização ---
        widget_frame = tk.Frame(canvas_bg, bg="#000000")
        window_item = canvas_bg.create_window(0, 0, window=widget_frame)

        def resize_widget_frame(event):
            w, h = event.width, event.height
            frame_width = int(w * 0.6)
            frame_height = int(h * 0.6)
            canvas_bg.itemconfig(window_item, width=frame_width, height=frame_height)
            canvas_bg.coords(window_item, w // 2, h // 2)
        canvas_bg.bind("<Configure>", resize_widget_frame)

        # --- Estilos Personalizados ---
        style = ttk.Style(self.master)
        style.configure("Search.TLabel",
                        background="#000000",
                        foreground="#00BFFF",
                        font=("Segoe UI", 20, "bold"))
        style.configure("Search.TButton",
                        background="#1E90FF",
                        foreground="white",
                        font=("Segoe UI", 20, "bold"),
                        padding=10)
        style.map("Search.TButton",
                background=[("active", "#00BFFF")])

        # --- Widgets da Interface ---
        lbl_search = ttk.Label(widget_frame, text="Nome do Serviço:", style="Search.TLabel",  font=("Segoe UI", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_search = ttk.Entry(widget_frame, width=40, font=("Segoe UI", 12), justify="center")
        self.entry_search.grid(row=0, column=1, padx=10, pady=10)

        btn_search = ttk.Button(widget_frame, text="Buscar", command=self.search_credential, style="Search.TButton")
        btn_search.grid(row=1, column=0, columnspan=2, pady=15)

        self.text_result = tk.Text(widget_frame, height=10, width=60, bg="#1C1C1C", fg="white",
                                font=("Roboto", 11), wrap="word", padx=10, pady=10)
        self.text_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.text_result.config(state=tk.DISABLED)

        # Centraliza os widgets no frame
        widget_frame.grid_columnconfigure(0, weight=1)
        widget_frame.grid_columnconfigure(1, weight=1)



    
    def search_credential(self):
        service = self.entry_search.get().strip()
        if service in self.credentials:
            cred = self.credentials[service]
            result = f"Serviço: {service}\nUsuário: {cred['username']}\nSenha: {cred['password']}"
        else:
            result = "Credencial não encontrada."
        self.text_result.config(state=tk.NORMAL)
        self.text_result.delete("1.0", tk.END)
        self.text_result.insert(tk.END, result)
        self.text_result.config(state=tk.DISABLED)
    
    # Aba para gerar senhas aleatórias customizadas
    def create_generate_tab(self):
        # Cria a aba "Gerar Senha" no Notebook
        self.generate_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.generate_tab, text="Gerar Senha")
        
        # --- Fundo Animado com Partículas Neon ---
        canvas_bg = tk.Canvas(self.generate_tab, bg="#000000", highlightthickness=0)
        canvas_bg.pack(fill="both", expand=True)
        
        particles = []
        num_particles = 30
        # Valores iniciais arbitrários; a animação se adapta ao tamanho do canvas
        for _ in range(num_particles):
            particles.append({
                "x": random.uniform(0, 800),
                "y": random.uniform(0, 600),
                "vx": random.uniform(-2, 2),
                "vy": random.uniform(-2, 2),
                "size": random.uniform(2, 4),
                "color": random.choice(["#00FFFF", "#00BFFF", "#1E90FF", "#40E0D0"])
            })
        
        def animate_particles():
            canvas_bg.delete("particle")
            w = canvas_bg.winfo_width()
            h = canvas_bg.winfo_height()
            for p in particles:
                p["x"] += p["vx"]
                p["y"] += p["vy"]
                # Realiza wrap-around para que as partículas reapareçam na tela
                if p["x"] < 0: p["x"] = w
                elif p["x"] > w: p["x"] = 0
                if p["y"] < 0: p["y"] = h
                elif p["y"] > h: p["y"] = 0
                canvas_bg.create_oval(
                    p["x"] - p["size"], p["y"] - p["size"],
                    p["x"] + p["size"], p["y"] + p["size"],
                    fill=p["color"], outline="", tags="particle"
                )
            canvas_bg.after(10, animate_particles)
        
        animate_particles()
        
        # --- Layout Responsivo e Centralização dos Controles ---
        widget_frame = tk.Frame(canvas_bg, bg="#000000")
        window_item = canvas_bg.create_window(0, 0, window=widget_frame)
        
        def resize_widget_frame(event):
            w, h = event.width, event.height
            # Define o widget_frame com 60% da largura e 60% da altura do canvas
            frame_width = int(w * 0.6)
            frame_height = int(h * 0.6)
            canvas_bg.itemconfig(window_item, width=frame_width, height=frame_height)
            canvas_bg.coords(window_item, w // 2, h // 2)
        canvas_bg.bind("<Configure>", resize_widget_frame)
        
        # --- Estilos Futuristas Personalizados ---
        style = ttk.Style(self.master)
        style.configure("Generate.TLabel",
                        background="#000000",
                        foreground="#00BFFF",
                        font=("Segoe UI", 20, "bold"))
        style.configure("Generate.TCheckbutton",
                        background="#000000",
                        foreground="#00BFFF",
                        font=("Segoe UI", 20))
        style.configure("Generate.TButton",
                        background="#1E90FF",
                        foreground="white",
                        font=("Segoe UI", 20, "bold"),
                        padding=10)
        style.map("Generate.TButton",
                background=[("active", "#00BFFF")])
        
        # --- Widgets da Interface ---
        # Linha 0: Label e controle customizado para o Tamanho da Senha
        lbl_length = ttk.Label(widget_frame, text="Tamanho da Senha:", style="Generate.TLabel", font=("Segoe UI", 20, "bold"))
        lbl_length.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        # Cria um frame para agrupar o campo de entrada e os botões de ajuste
        spin_frame = tk.Frame(widget_frame, bg="#000000")
        spin_frame.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        
        # Variável para armazenar o valor do tamanho da senha
        self.spin_length_var = tk.IntVar(value=6)
        # Campo de entrada (mantém o nome para compatibilidade)
        self.spin_length = ttk.Entry(spin_frame, textvariable=self.spin_length_var,
                                    width=5, font=("Segoe UI", 20), justify="center")
        self.spin_length.grid(row=0, column=0, rowspan=2, padx=(0,5))
        
        # Botão para aumentar o valor (limite máximo 32)
        btn_increase = ttk.Button(spin_frame, text="+", width=1,
        
                                command=lambda: self.spin_length_var.set(min(self.spin_length_var.get() + 1, 32)),
                                style="Generate.TButton")
        btn_increase.grid(row=0, column=1, padx=1, pady=1)
        
        # Botão para diminuir o valor (limite mínimo 6)
        btn_decrease = ttk.Button(spin_frame, text="-",width=1,
                                command=lambda: self.spin_length_var.set(max(self.spin_length_var.get() - 1, 6)),
                                style="Generate.TButton")
        btn_decrease.grid(row=1, column=1, padx=1, pady=1)
        
        # Linha 1: Checkbuttons para incluir símbolos e números
        self.var_symbols = tk.BooleanVar(value=True)
        chk_symbols = ttk.Checkbutton(widget_frame, text="Incluir Símbolos",
                                    variable=self.var_symbols, style="Generate.TCheckbutton")
        chk_symbols.grid(row=1, column=0, padx=1, pady=10, sticky="e")
        
        self.var_numbers = tk.BooleanVar(value=True)
        chk_numbers = ttk.Checkbutton(widget_frame, text="Incluir Números",
                                    variable=self.var_numbers, style="Generate.TCheckbutton")
        chk_numbers.grid(row=1, column=1, padx=1, pady=10, sticky="w")
        
        # Linha 2: Botão para gerar a senha
        btn_generate = ttk.Button(widget_frame, text="Gerar Senha",
                                command=self.generate_password, style="Generate.TButton")
        btn_generate.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Linha 3: Campo para exibir a senha gerada (centralizado)
        self.entry_generated = ttk.Entry(widget_frame, width=40, font=("Segoe UI", 12), justify="center")
        self.entry_generated.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # Centraliza os widgets no frame
        widget_frame.grid_columnconfigure(0, weight=1)
        widget_frame.grid_columnconfigure(1, weight=1)

    def generate_password(self):
        length = int(self.spin_length.get())
        use_symbols = self.var_symbols.get()
        use_numbers = self.var_numbers.get()
        pwd = generate_random_password(length, use_symbols, use_numbers)
        self.entry_generated.delete(0, tk.END)
        self.entry_generated.insert(0, pwd)
    
    # Aba para listar todas as credenciais salvas
    def create_list_tab(self):
        # Cria a aba "Listar Credenciais" no Notebook
        self.list_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.list_tab, text="Listar Credenciais")
        
        # --- Fundo Animado com Partículas Neon ---
        # Um Canvas cobre toda a aba e renderiza partículas em movimento
        canvas_bg = tk.Canvas(self.list_tab, bg="#000000", highlightthickness=0)
        canvas_bg.pack(fill="both", expand=True)
        
        # Inicializa as partículas com atributos: posição, velocidade, tamanho e cor neon
        particles = []
        num_particles = 50
        default_width, default_height = 1600, 1200  # Valores iniciais padrão
        for _ in range(num_particles):
            particles.append({
                "x": random.uniform(0, default_width),
                "y": random.uniform(0, default_height),
                "vx": random.uniform(-2, 2),
                "vy": random.uniform(-2, 2),
                "size": random.uniform(2, 4),
                "color": random.choice(["#00FFFF", "#00BFFF", "#1E90FF", "#40E0D0"])
            })
        
        def animate_particles():
            canvas_bg.delete("particle")
            w = canvas_bg.winfo_width()
            h = canvas_bg.winfo_height()
            for p in particles:
                # Atualiza a posição da partícula
                p["x"] += p["vx"]
                p["y"] += p["vy"]
                # Se sair da área, faz o wrap-around
                if p["x"] < 0:
                    p["x"] = w
                elif p["x"] > w:
                    p["x"] = 0
                if p["y"] < 0:
                    p["y"] = h
                elif p["y"] > h:
                    p["y"] = 0
                # Desenha a partícula com um efeito neon
                canvas_bg.create_oval(
                    p["x"] - p["size"], p["y"] - p["size"],
                    p["x"] + p["size"], p["y"] + p["size"],
                    fill=p["color"], outline="", tags="particle"
                )
            canvas_bg.after(30, animate_particles)
        
        animate_particles()
        
        # --- Layout Responsivo ---
        # Cria um frame para os widgets da interface que será posicionado no centro do Canvas.
        # Para permitir a visualização do fundo animado, o frame terá tamanho relativo à janela.
        widget_frame = tk.Frame(canvas_bg, bg="#000000")
        # Inicialmente posiciona o frame no centro do canvas
        window_item = canvas_bg.create_window(
            canvas_bg.winfo_width() // 2,
            canvas_bg.winfo_height() // 2,
            window=widget_frame
        )
        
        def resize_widget_frame(event):
            w, h = event.width, event.height
            # Define o widget_frame com 80% da largura e 70% da altura do canvas
            frame_width = int(w * 0.8)
            frame_height = int(h * 0.7)
            canvas_bg.itemconfig(window_item, width=frame_width, height=frame_height)
            canvas_bg.coords(window_item, w // 2, h // 2)
        canvas_bg.bind("<Configure>", resize_widget_frame)
        
        # --- Estilos Futuristas Personalizados ---
        style = ttk.Style(self.master)
        
        # Estilo para o Checkbutton (texto em tom de azul neon)
        style.configure("Futuristic.TCheckbutton",
                        background="#000000",
                        foreground="#00BFFF",
                        font=("Segoe UI", 15))
        
        # Estilo para os Botões com aparência moderna
        style.configure("Futuristic.TButton",
                        background="#1E90FF",
                        foreground="white",
                        font=("Segoe UI", 15, "bold"),
                        padding=10)
        style.map("Futuristic.TButton",
                background=[("active", "#00BFFF")])
        
        # Estilo para o Treeview: fundo preto, linhas em branco e headers com texto branco
        style.configure("Futuristic.Treeview",
                        background="#000000",
                        foreground="white",
                        fieldbackground="#000000",
                        bordercolor="#00BFFF",
                        borderwidth=1,
                        rowheight=30)
        style.configure("Futuristic.Treeview.Heading",
                        background="#1E90FF",
                        foreground="white",  # Headers com letras brancas
                        font=("Segoe UI", 15, "bold"))
        
        # Estilo para a Scrollbar
        style.configure("Futuristic.Vertical.TScrollbar",
                        background="#000000",
                        troughcolor="#000000",
                        arrowcolor="#00BFFF")
        
        # --- Widgets da Interface ---
        # Checkbox para mostrar/ocultar as senhas
        self.show_passwords = tk.BooleanVar(value=False)
        chk_show = ttk.Checkbutton(widget_frame, text="Mostrar Senhas", variable=self.show_passwords,
                                command=self.refresh_list_tab, style="Futuristic.TCheckbutton")
        chk_show.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Botão para atualizar a lista de credenciais
        btn_refresh = ttk.Button(widget_frame, text="Atualizar Lista",
                                command=self.refresh_list_tab, style="Futuristic.TButton")
        btn_refresh.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        
        # Treeview para exibir as credenciais
        columns = ("Serviço", "Usuário", "Senha")
        self.tree = ttk.Treeview(widget_frame, columns=columns, show="headings", style="Futuristic.Treeview")
        for col in columns:
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, anchor="center", width=150)
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        # Scrollbar vertical para o Treeview
        scrollbar = ttk.Scrollbar(widget_frame, orient=tk.VERTICAL, command=self.tree.yview,
                                style="Futuristic.Vertical.TScrollbar")
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky="ns")
        
        # Permite copiar a credencial com duplo clique
        self.tree.bind("<Double-1>", self.copy_selected_credential)
        
        # Configura o layout responsivo dentro do widget_frame
        widget_frame.grid_rowconfigure(1, weight=1)
        widget_frame.grid_columnconfigure(0, weight=1)
        
        self.refresh_list_tab()



    def refresh_list_tab(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.credentials = load_credentials(self.fernet)
        for service, data in self.credentials.items():
            pwd_disp = data["password"] if self.show_passwords.get() else "*" * len(data["password"])
            self.tree.insert("", tk.END, values=(service, data["username"], pwd_disp))
    
    def copy_selected_credential(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            service, username, password = item["values"]
            # Copia a senha real para a área de transferência
            cred = self.credentials.get(service, {})
            real_password = cred.get("password", "")
            self.master.clipboard_clear()
            self.master.clipboard_append(real_password)
            messagebox.showinfo("Copiado", "Senha copiada para a área de transferência!")
    
    def add_credential(self):
        service = self.entry_service.get().strip()
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        if not service or not username or not password:
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos.")
            return
        self.credentials[service] = {"username": username, "password": password}
        save_credentials(self.credentials, self.fernet)
        messagebox.showinfo("Sucesso", f"Credencial para {service} adicionada com sucesso!")
        self.entry_service.delete(0, tk.END)
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.refresh_list_tab()



def launch_app(master_password: str):
    key = derive_key(master_password)
    fernet = Fernet(key)
    root = tk.Tk()
    root.title("J.A.R.V.I.S.")
    root.attributes('-fullscreen', True)
    root.configure(bg="#0A0E14")
    # Centraliza a janela na tela
    root.eval('tk::PlaceWindow . center')
    app = PasswordManagerApp(root, fernet)
    # Alterna o modo fullscreen com F11 e retorna com Esc
    root.bind("<F11>", lambda event: root.attributes('-fullscreen', not root.attributes('-fullscreen')))
    root.bind("<Escape>", lambda event: root.attributes('-fullscreen', False))
    root.mainloop()

def login_window():
    login = tk.Tk()
    login.title("Autenticação - J.A.R.V.I.S.")
    login.attributes('-fullscreen', True)
    login.configure(bg="#0A0E14")
    login.eval('tk::PlaceWindow . center')

    # Cria um canvas para as animações de fundo
    canvas = tk.Canvas(login, bg="#0A0E14", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    width = login.winfo_screenwidth()
    height = login.winfo_screenheight()
    
    # Cria um sistema de partículas para o fundo animado
    particles = []
    num_particles = 50
    for _ in range(num_particles):
        particles.append({
            'x': random.uniform(0, width),
            'y': random.uniform(0, height),
            'vx': random.uniform(-1, 1),
            'vy': random.uniform(-1, 1),
            'size': random.uniform(2, 4),
            'life': random.uniform(50, 100),
            'color': random.choice(["#0074E8", "#1A8CFF", "#4DA6FF", "#80BFFF"])
        })
    
    def animate_login_background():
        canvas.delete("bg")
        # Cria um gradiente vertical
        steps = 50
        for i in range(steps):
            intensity = i / steps
            color = f"#0000{int(intensity * 255):02x}"
            y1 = i * (height / steps)
            y2 = (i + 1) * (height / steps)
            canvas.create_rectangle(0, y1, width, y2, fill=color, outline="", tags="bg")
        # Atualiza as partículas
        for p in particles:
            p['x'] += p['vx']
            p['y'] += p['vy']
            p['life'] -= 1
            if p['life'] <= 0:
                p['x'] = random.uniform(0, width)
                p['y'] = random.uniform(0, height)
                p['life'] = random.uniform(50, 100)
            canvas.create_oval(p['x'] - p['size'], p['y'] - p['size'],
                               p['x'] + p['size'], p['y'] + p['size'],
                               fill=p['color'], outline="", tags="bg")
        canvas.after(50, animate_login_background)
    
    animate_login_background()
    
    # Cria um frame para os widgets de autenticação e centraliza-o no canvas
    frame = tk.Frame(login, bg="#0A0E14")
    center_x = width // 2
    center_y = height // 2
    canvas.create_window(center_x, center_y, window=frame, width=1200, height=250)
    
    # Define a função de autenticação
    def attempt_login():
        pwd = entry_master.get()
        if os.path.exists(MASTER_HASH_FILE):
            if check_master_password(pwd):
                login.destroy()
                launch_app(pwd)
            else:
                messagebox.showerror("Erro", "Senha mestra incorreta!")
        else:
            confirm = simpledialog.askstring("Confirmação", "Confirme a nova senha mestra:", show="*", parent=login)
            if pwd == confirm and pwd != "":
                set_master_password(pwd)
                messagebox.showinfo("Sucesso", "Senha mestra configurada com sucesso!")
                login.destroy()
                launch_app(pwd)
            else:
                messagebox.showerror("Erro", "As senhas não conferem ou estão vazias.")
    
    # Exibe uma mensagem aleatória de boas-vindas
    welcome_messages = [
        "Olá, Arthur. Por favor, insira suas credenciais para iniciar.",
        "Olá, Arthur. Autenticação necessária para continuar.",
        "Ação requerida, Arthur. Insira suas credenciais de acesso.",
        "Bem-vindo de volta, Arthur. Por favor, autentique-se para prosseguir."
    ]
    welcome_msg = random.choice(welcome_messages)
    lbl_welcome = ttk.Label(frame, text=welcome_msg, anchor="center",
                            background="#0A0E14", foreground="#3498DB", font=("Segoe UI", 25, "bold"))
    lbl_welcome.pack(pady=(20, 10))
    
    # Campo de digitação da senha centralizado com efeito holográfico
    # Usamos tk.Entry para facilitar a animação do texto
    entry_master = tk.Entry(frame, show="*", width=30, font=("Segoe UI", 25),
                            justify="center", bd=0, relief="flat")
    entry_master.pack(pady=10)
    
    # Animação do efeito holográfico: as cores do texto vão alternando periodicamente
    holographic_colors = ["#0074E8", "#1A8CFF", "#4DA6FF", "#80BFFF"]
    holo_index = 0
    def animate_entry_text_color():
        nonlocal holo_index
        entry_master.config(fg=holographic_colors[holo_index])
        holo_index = (holo_index + 1) % len(holographic_colors)
        login.after(200, animate_entry_text_color)
    animate_entry_text_color()
    
    btn_login = ttk.Button(frame, text="Entrar", command=attempt_login, style="TButton")
    btn_login.pack(pady=20)
    
    login.mainloop()

if __name__ == "__main__":
    login_window()
