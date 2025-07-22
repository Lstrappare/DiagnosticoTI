import os
import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Importa ttkbootstrap para temas y widgets modernos
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# --- Lógica de Backend (Funciones originales sin cambios) ---

USUARIOS_FILE = "usuarios.txt"

def registrar_usuario(usuario, contraseña):
    """Registra un nuevo usuario en el archivo."""
    if existe_usuario(usuario):
        return "exists"
    with open(USUARIOS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{usuario},{contraseña}\n")
    return "success"

def existe_usuario(usuario):
    """Verifica si un usuario ya existe."""
    if not os.path.exists(USUARIOS_FILE):
        return False
    with open(USUARIOS_FILE, "r", encoding="utf-8") as f:
        for linea in f:
            u, _ = linea.strip().split(",")
            if u == usuario:
                return True
    return False

def login_usuario(usuario, contraseña):
    """Valida las credenciales del usuario."""
    if not os.path.exists(USUARIOS_FILE):
        return False
    with open(USUARIOS_FILE, "r", encoding="utf-8") as f:
        for linea in f:
            u, c = linea.strip().split(",")
            if u == usuario and c == contraseña:
                return True
    return False

def mostrar_recomendaciones(resultados_cobit, resultados_cmmi):
    """Genera el texto de recomendaciones basado en los resultados."""
    recomendaciones = "Recomendaciones basadas en tu diagnóstico:\n\n"
    recomendaciones += "🔹 COBIT:\n"
    for dimension, puntaje in resultados_cobit.items():
        if puntaje < 3:
            recomendaciones += f"  🔻 {dimension}: Nivel bajo ({puntaje}/5). Requiere atención prioritaria.\n"
        else:
            recomendaciones += f"  ✅ {dimension}: Nivel aceptable ({puntaje}/5).\n"
    recomendaciones += "\n🔹 CMMI:\n"
    for proceso, (nivel, desc) in resultados_cmmi.items():
        if nivel < 3:
            recomendaciones += f"  🔻 {proceso}: Nivel {nivel} ({desc}). Se recomienda formalizar y documentar procesos.\n"
        else:
            recomendaciones += f"  ✅ {proceso}: Nivel {nivel} ({desc}).\n"
    return recomendaciones

def graficar_cobit(resultados_cobit, frame):
    """Crea y muestra el gráfico de barras de COBIT en la interfaz."""
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(5, 4), facecolor='#ffffff')
    ax.set_facecolor('#ffffff')
    
    dimensiones = list(resultados_cobit.keys())
    puntajes = list(resultados_cobit.values())
    
    ax.bar(dimensiones, puntajes, color='#0d6efd')
    ax.set_title("Resultados de Evaluación COBIT", fontweight='bold')
    ax.set_ylabel("Nivel de Madurez (1-5)")
    ax.set_ylim(0, 5)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    fig.tight_layout()
    
    canvas_agg = FigureCanvasTkAgg(fig, master=frame)
    canvas_agg.draw()
    canvas_agg.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)

def graficar_cmmi(resultados_cmmi, frame):
    """Crea y muestra el gráfico de barras de CMMI en la interfaz."""
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(5, 4), facecolor='#ffffff')
    ax.set_facecolor('#ffffff')
    
    procesos = list(resultados_cmmi.keys())
    niveles = [nivel for nivel, _ in resultados_cmmi.values()]

    ax.bar(procesos, niveles, color='#dc3545')
    ax.set_title("Resultados de Evaluación CMMI", fontweight='bold')
    ax.set_ylabel("Nivel de Madurez (1-5)")
    ax.set_ylim(0, 5)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    fig.tight_layout()

    canvas_agg = FigureCanvasTkAgg(fig, master=frame)
    canvas_agg.draw()
    canvas_agg.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)
    
def exportar_csv(usuario, resultados_cobit, resultados_cmmi):
    """Exporta los resultados a un archivo CSV."""
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"diagnostico_{usuario}_{fecha}.csv"
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Reporte de Diagnóstico de Administración Informática"])
        writer.writerow(["Usuario:", usuario])
        writer.writerow(["Fecha:", fecha])
        writer.writerow([])
        writer.writerow(["Resultados COBIT"])
        writer.writerow(["Dimensión", "Nivel (1-5)"])
        for dimension, puntaje in resultados_cobit.items():
            writer.writerow([dimension, puntaje])
        writer.writerow([])
        writer.writerow(["Resultados CMMI"])
        writer.writerow(["Proceso", "Nivel", "Descripción"])
        for proceso, (nivel, desc) in resultados_cmmi.items():
            writer.writerow([proceso, nivel, desc])
    return nombre_archivo

def exportar_pdf(usuario, resultados_cobit, resultados_cmmi):
    """Exporta los resultados a un archivo PDF."""
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nombre_archivo = f"diagnostico_{usuario}_{fecha}.pdf"
    # El resto de la función es idéntica y no necesita cambios
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    ancho, alto = A4
    y = alto - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Reporte de Diagnóstico de Administración Informática")
    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Usuario: {usuario}")
    y -= 20
    c.drawString(50, y, f"Fecha: {fecha}")
    y -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Resultados COBIT:")
    y -= 20
    c.setFont("Helvetica", 11)
    for dimension, puntaje in resultados_cobit.items():
        c.drawString(60, y, f"- {dimension}: Nivel {puntaje}/5")
        y -= 15
    y -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Resultados CMMI:")
    y -= 20
    c.setFont("Helvetica", 11)
    for proceso, (nivel, desc) in resultados_cmmi.items():
        c.drawString(60, y, f"- {proceso}: Nivel {nivel} - {desc}")
        y -= 15
    c.save()
    return nombre_archivo

# --- Clase de la Aplicación GUI Moderna ---
class ModernDiagnosticApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Herramienta de Diagnóstico de TI")
        self.root.geometry("1200x800")
        
        self.current_user = None
        self.cobit_results = {}
        self.cmmi_results = {}
        self.cobit_vars = {}
        self.cmmi_vars = {}

        self.main_container = ttk.Frame(self.root, padding=20)
        self.main_container.pack(fill=BOTH, expand=YES)

        self.create_auth_frame()
        self.create_app_frame()
        
        self.show_frame(self.auth_frame)

    def show_frame(self, frame_to_show):
        """Muestra el frame seleccionado y oculta los otros."""
        self.auth_frame.pack_forget()
        self.app_frame.pack_forget()
        frame_to_show.pack(fill=BOTH, expand=YES)

    # --- Pantallas de Autenticación ---
    def create_auth_frame(self):
        self.auth_frame = ttk.Frame(self.main_container)
        self.login_view = self.create_login_view(self.auth_frame)
        self.register_view = self.create_register_view(self.auth_frame)
        self.login_view.pack(fill=BOTH, expand=YES)

    def show_login_view(self):
        self.register_view.pack_forget()
        self.login_view.pack(fill=BOTH, expand=YES)
        self.root.title("Iniciar Sesión")

    def show_register_view(self):
        self.login_view.pack_forget()
        self.register_view.pack(fill=BOTH, expand=YES)
        self.root.title("Registro de Usuario")

    def create_login_view(self, parent):
        frame = ttk.Frame(parent)
        center_frame = ttk.Frame(frame)
        center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        header = ttk.Label(center_frame, text="Iniciar Sesión", font=("Helvetica", 24, "bold"), bootstyle=PRIMARY)
        header.pack(pady=20)
        user_frame = ttk.Frame(center_frame); user_frame.pack(pady=10, padx=20, fill=X)
        ttk.Label(user_frame, text="Usuario:", width=10).pack(side=LEFT)
        self.usuario_entry = ttk.Entry(user_frame, bootstyle=PRIMARY)
        self.usuario_entry.pack(side=LEFT, fill=X, expand=YES)
        pass_frame = ttk.Frame(center_frame); pass_frame.pack(pady=10, padx=20, fill=X)
        ttk.Label(pass_frame, text="Contraseña:", width=10).pack(side=LEFT)
        self.contraseña_entry = ttk.Entry(pass_frame, show="*", bootstyle=PRIMARY)
        self.contraseña_entry.pack(side=LEFT, fill=X, expand=YES)
        ttk.Button(center_frame, text="Entrar", command=self.handle_login, bootstyle=SUCCESS).pack(fill=X, padx=20, pady=10)
        ttk.Button(center_frame, text="Crear una cuenta", command=self.show_register_view, bootstyle=(LINK, PRIMARY)).pack(pady=5)
        return frame

    def create_register_view(self, parent):
        frame = ttk.Frame(parent)
        center_frame = ttk.Frame(frame)
        center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        header = ttk.Label(center_frame, text="Crear Cuenta", font=("Helvetica", 24, "bold"), bootstyle=PRIMARY)
        header.pack(pady=20)
        user_frame = ttk.Frame(center_frame); user_frame.pack(pady=10, padx=20, fill=X)
        ttk.Label(user_frame, text="Usuario:", width=10).pack(side=LEFT)
        self.reg_usuario_entry = ttk.Entry(user_frame, bootstyle=PRIMARY)
        self.reg_usuario_entry.pack(side=LEFT, fill=X, expand=YES)
        pass_frame = ttk.Frame(center_frame); pass_frame.pack(pady=10, padx=20, fill=X)
        ttk.Label(pass_frame, text="Contraseña:", width=10).pack(side=LEFT)
        self.reg_contraseña_entry = ttk.Entry(pass_frame, show="*", bootstyle=PRIMARY)
        self.reg_contraseña_entry.pack(side=LEFT, fill=X, expand=YES)
        ttk.Button(center_frame, text="Registrar", command=self.handle_register, bootstyle=SUCCESS).pack(fill=X, padx=20, pady=10)
        ttk.Button(center_frame, text="Ya tengo una cuenta", command=self.show_login_view, bootstyle=(LINK, PRIMARY)).pack(pady=5)
        return frame

    def handle_login(self):
        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()
        if not usuario or not contraseña:
            messagebox.showerror("Error", "Por favor, ingrese usuario y contraseña.")
            return
        if login_usuario(usuario, contraseña):
            self.current_user = usuario
            self.user_label.config(text=f"Usuario: {self.current_user}")
            self.show_frame(self.app_frame)
            self.root.title(f"Diagnóstico de TI - {self.current_user}")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def handle_register(self):
        usuario = self.reg_usuario_entry.get()
        contraseña = self.reg_contraseña_entry.get()
        if not usuario or not contraseña:
            messagebox.showerror("Error", "Usuario y contraseña no pueden estar vacíos.")
            return
        result = registrar_usuario(usuario, contraseña)
        if result == "success":
            messagebox.showinfo("Éxito", "Usuario registrado. Ahora puede iniciar sesión.")
            self.show_login_view()
        else:
            messagebox.showerror("Error", "El usuario ya existe. Intente con otro nombre.")

    def handle_logout(self):
        self.current_user = None
        self.usuario_entry.delete(0, END); self.contraseña_entry.delete(0, END)
        self.reg_usuario_entry.delete(0, END); self.reg_contraseña_entry.delete(0, END)
        self.cobit_results.clear(); self.cmmi_results.clear()
        self.notebook.select(0)
        self.notebook.tab(1, state=DISABLED)
        self.show_frame(self.auth_frame)
        self.root.title("Herramienta de Diagnóstico de TI")

    # --- Pantallas de la Aplicación Principal ---
    def create_app_frame(self):
        self.app_frame = ttk.Frame(self.main_container)
        header_frame = ttk.Frame(self.app_frame); header_frame.pack(fill=X, pady=(0, 10))
        self.user_label = ttk.Label(header_frame, text="Usuario: ", font=("Helvetica", 12))
        self.user_label.pack(side=LEFT)
        ttk.Button(header_frame, text="Cerrar Sesión", command=self.handle_logout, bootstyle=DANGER).pack(side=RIGHT)
        self.notebook = ttk.Notebook(self.app_frame, bootstyle=PRIMARY)
        self.notebook.pack(fill=BOTH, expand=YES)
        self.eval_frame = ttk.Frame(self.notebook, padding=10)
        self.results_frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.eval_frame, text='📝 Evaluaciones')
        self.notebook.add(self.results_frame, text='📊 Resultados', state=DISABLED)
        self.create_evaluation_tabs(self.eval_frame)
        self.create_results_display(self.results_frame)

    def create_evaluation_tabs(self, parent):
        eval_notebook = ttk.Notebook(parent)
        eval_notebook.pack(fill=BOTH, expand=YES, padx=5, pady=5)
        cobit_tab = ttk.Frame(eval_notebook, padding=15)
        cmmi_tab = ttk.Frame(eval_notebook, padding=15)
        eval_notebook.add(cobit_tab, text='COBIT')
        eval_notebook.add(cmmi_tab, text='CMMI')
        self.populate_cobit_tab(cobit_tab)
        self.populate_cmmi_tab(cmmi_tab)
        ttk.Button(parent, text="Generar Diagnóstico", command=self.process_evaluations, bootstyle=(SUCCESS, OUTLINE)).pack(pady=20)

    def populate_cobit_tab(self, parent):
        """
        *** CAMBIO REALIZADO AQUÍ ***
        Esta función ahora crea botones de radio (igual que CMMI) en lugar de sliders.
        """
        preguntas_cobit = {
            "Alineación Estratégica": "¿Cuál es el nivel de madurez en Alineación Estratégica?",
            "Entrega de Valor": "¿Cuál es el nivel de madurez en la Entrega de Valor de TI?",
            "Gestión de Riesgos": "¿Cuál es el nivel de madurez en la Gestión de Riesgos de TI?",
            "Gestión de Recursos": "¿Cuál es el nivel de madurez en la Gestión de Recursos de TI?",
            "Medición del Desempeño": "¿Cuál es el nivel de madurez en la Medición del Desempeño de TI?"
        }
        self.cobit_vars = {}
        for dimension, pregunta in preguntas_cobit.items():
            frame = ttk.LabelFrame(parent, text=f"📂 {dimension}", bootstyle=INFO, padding=10)
            frame.pack(fill=X, expand=YES, pady=5)
            ttk.Label(frame, text=pregunta).pack(anchor=W)
            var = tk.IntVar(value=3)
            self.cobit_vars[dimension] = var
            radio_frame = ttk.Frame(frame)
            radio_frame.pack(fill=X, pady=5)
            for j in range(1, 6):
                ttk.Radiobutton(radio_frame, text=str(j), variable=var, value=j, bootstyle=(TOOLBUTTON, PRIMARY)).pack(side=LEFT, padx=5, fill=X, expand=YES)

    def populate_cmmi_tab(self, parent):
        """Esta función permanece igual, sirviendo como modelo para la de COBIT."""
        procesos = {
            "Gestión de Proyectos": "¿Nivel de madurez en gestión de proyectos?",
            "Gestión de Requisitos": "¿Nivel de madurez en gestión de requisitos?",
            "Desarrollo de Software": "¿Nivel de madurez en desarrollo de software?",
            "Aseguramiento de Calidad": "¿Nivel de madurez del aseguramiento de calidad?",
            "Gestión de Configuración": "¿Nivel de madurez en gestión de configuración?"
        }
        self.cmmi_vars = {}
        for proceso, pregunta in procesos.items():
            frame = ttk.LabelFrame(parent, text=f"📈 {proceso}", bootstyle=INFO, padding=10)
            frame.pack(fill=X, expand=YES, pady=5)
            ttk.Label(frame, text=pregunta).pack(anchor=W)
            var = tk.IntVar(value=3)
            self.cmmi_vars[proceso] = var
            radio_frame = ttk.Frame(frame)
            radio_frame.pack(fill=X, pady=5)
            for j in range(1, 6):
                ttk.Radiobutton(radio_frame, text=str(j), variable=var, value=j, bootstyle=(TOOLBUTTON, PRIMARY)).pack(side=LEFT, padx=5, fill=X, expand=YES)

    def process_evaluations(self):
        """
        *** CAMBIO REALIZADO AQUÍ ***
        La lógica de COBIT ahora obtiene el valor directo del botón, igual que CMMI.
        """
        # Procesar COBIT
        for dimension, var in self.cobit_vars.items():
            self.cobit_results[dimension] = var.get()
        # Procesar CMMI
        niveles = {1: "Inicial", 2: "Gestionado", 3: "Definido", 4: "Cuantitativamente gestionado", 5: "Optimizado"}
        for proceso, var in self.cmmi_vars.items():
            nivel_val = var.get()
            self.cmmi_results[proceso] = (nivel_val, niveles[nivel_val])
        self.update_results_display()
        self.notebook.tab(1, state=NORMAL)
        self.notebook.select(1)

    def create_results_display(self, parent):
        parent.columnconfigure(0, weight=1); parent.columnconfigure(1, weight=1)
        parent.rowconfigure(0, weight=1)
        graphs_container = ttk.Frame(parent); graphs_container.grid(row=0, column=0, sticky=NSEW, padx=(0, 10))
        self.cobit_graph_frame = ttk.LabelFrame(graphs_container, text="Gráfico COBIT", bootstyle=PRIMARY, padding=10)
        self.cobit_graph_frame.pack(fill=BOTH, expand=YES, pady=(0, 5))
        self.cmmi_graph_frame = ttk.LabelFrame(graphs_container, text="Gráfico CMMI", bootstyle=DANGER, padding=10)
        self.cmmi_graph_frame.pack(fill=BOTH, expand=YES, pady=(5, 0))
        info_container = ttk.Frame(parent); info_container.grid(row=0, column=1, sticky=NSEW, padx=(10, 0))
        recom_frame = ttk.LabelFrame(info_container, text="💡 Recomendaciones", bootstyle=SUCCESS, padding=15)
        recom_frame.pack(fill=BOTH, expand=YES)
        self.recom_label = ttk.Label(recom_frame, text="Complete las evaluaciones para ver las recomendaciones.", wraplength=500, justify=LEFT)
        self.recom_label.pack(fill=BOTH, expand=YES)
        export_frame = ttk.Frame(info_container); export_frame.pack(fill=X, pady=10)
        ttk.Button(export_frame, text="Exportar a CSV", command=self.handle_export_csv, bootstyle=SECONDARY).pack(side=LEFT, expand=YES, padx=5)
        ttk.Button(export_frame, text="Exportar a PDF", command=self.handle_export_pdf, bootstyle=SECONDARY).pack(side=LEFT, expand=YES, padx=5)

    def update_results_display(self):
        for widget in self.cobit_graph_frame.winfo_children(): widget.destroy()
        for widget in self.cmmi_graph_frame.winfo_children(): widget.destroy()
        graficar_cobit(self.cobit_results, self.cobit_graph_frame)
        graficar_cmmi(self.cmmi_results, self.cmmi_graph_frame)
        self.recom_label.config(text=mostrar_recomendaciones(self.cobit_results, self.cmmi_results))
        
    def handle_export_csv(self):
        if not self.cobit_results:
            messagebox.showwarning("Sin Datos", "Debe generar un diagnóstico antes de exportar.")
            return
        filename = exportar_csv(self.current_user, self.cobit_results, self.cmmi_results)
        messagebox.showinfo("Éxito", f"Resultados exportados a:\n{os.path.abspath(filename)}")

    def handle_export_pdf(self):
        if not self.cobit_results:
            messagebox.showwarning("Sin Datos", "Debe generar un diagnóstico antes de exportar.")
            return
        filename = exportar_pdf(self.current_user, self.cobit_results, self.cmmi_results)
        messagebox.showinfo("Éxito", f"Resultados exportados a:\n{os.path.abspath(filename)}")


if __name__ == "__main__":
    # Inicia la ventana con el tema 'litera'
    root = ttk.Window(themename="litera") 
    app = ModernDiagnosticApp(root)
    root.mainloop()